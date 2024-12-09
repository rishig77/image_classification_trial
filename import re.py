import re

text = """
Cookie Notice
We use cookies on this site. By continuing to browse without changing your browser settings to block or delete cookies, you agree to the UW–Madison Cookie Notice.
Accept cookie notice
Skip to main content
University of Wisconsin–Madison
Department of Economics
Search
Search
Undergraduate
MS in Economics
MS in Financial Economics
Doctoral
Career Services
Diversity
People
Alumni
Workshops/Events
JPGI
Donate
Home
Faculty
Faculty

Miguel Acosta
Position title:Assistant Professor

Email:miguel.acosta@wisc.edu

Phone:608-265-3137

Fields: Macroeconomics, International Trade

Website


Naoki Aizawa
Position title:Associate Professor

Email:naizawa@wisc.edu

Phone:608-262-9250

Pronouns: he/him/his

Fields: Labor Economics, Health Economics, Public Economics

Website

Simeon
Simeon Alder
Position title:Faculty Associate

Email:sdalder@wisc.edu

Phone:608-262-0488

Pronouns: he/him/his

Fields: Macroeconomics, Growth and Development, Matching


Panle Barwick
Position title:Professor, Todd E. and Elizabeth H. Warnock Distinguished Chair

Email:pbarwick@wisc.edu

Phone:608-264-2973

Fields: Industrial Organization, Applied Microeconomics, Environmental Econometrics

Website


Benjamin Bernard
Position title:Assistant Professor

Email:bbernard3@wisc.edu

Phone:608-263-6333

Fields: Game Theory, Microeconomic Theory, Financial Economics

Website


Job Boerma
Position title:Assistant Professor

Email:job.boerma@wisc.edu

Pronouns: he/him/his

Fields: Macroeconomics, Public Finance

Website


John Brauer
Position title:Lecturer

Email:jbrauer@wisc.edu

Phone:608-262-3676

Fields: Labor, Public

Website


Carter Braxton
Position title:Assistant Professor

Email:jcbraxton@wisc.edu

Phone:608-265-2620

Pronouns: he/him/his

Fields: Macroeconomics, Labor Economics, Consumer Finance

Website


Yong Cai
Position title:Assistant Professor

Email:yong.cai@wisc.edu

Fields: Econometrics

Website


Matteo Camboni
Position title:Assistant Professor

Email:camboni@wisc.edu

Phone:608-890-3684

Fields: Microeconomic Theory, Economics of Organizations

Website


Stella Chan
Position title:Lecturer

Email:mschan3@wisc.edu

Pronouns: she/her/hers


Harold Chiang
Position title:Assistant Professor

Email:hdchiang@wisc.edu

Phone:608-263-4202

Pronouns: he/him/his

Fields: Econometrics

Website

menzie chinn
Menzie Chinn
Position title:Professor

Email:mchinn@lafollette.wisc.edu

Phone:608-262-7397

Pronouns: he/him/his

Website

Corbae, Dean
Dean Corbae
Position title:Professor, William Sellery Trukenbrod Chair in Finance

Email:corbae@ssc.wisc.edu

Phone:608-262-3281

Pronouns: he/him/his

Fields: Macroeconomics

Website


Louphou Coulibaly
Position title:Assistant Professor

Email:lcoulibaly@wisc.edu

Phone:608-265-6594

Pronouns: he/him/his

Fields: International Economics, Macroeconomics

Website


Lydia Cox
Position title:Assistant Professor

Email:lydia.cox@wisc.edu

Phone:608-265-2570

Fields: International Trade and Macroeconomics

Website

Deneckere, Raymond
Raymond Deneckere
Position title:Professor

Email:rjdeneck@wisc.edu

Phone:608-263-6724

Fields: Microeconomic Theory, Industrial Organization

Engel, Charles
Charles Engel
Position title:Professor, Donald D. Hester Distinguished Chair

Email:cengel@ssc.wisc.edu

Phone:608-262-3697

Pronouns: he/him/his

Fields: International Economics, Macroeconomics

Website

Eudey, Gwen
Gwen Eudey
Position title:Senior Lecturer

Email:gwen.eudey@wisc.edu

Fields: Open Economy Macroeconomics


Fran Flanagan
Position title:Lecturer

Email:fflanagan@wisc.edu

Phone:608-263-2989

Pronouns: he/him/his

Fields: Micro Theory, Law, Market Design

Website


Matt Friedman
Position title:Lecturer

Email:mlfriedman@wisc.edu

Phone:608-265-6788

Chao Fu
Chao Fu
Position title:Professor, Mary Claire Aschenbrener Phipps Distinguished Chair

Email:cfu@ssc.wisc.edu

Phone:608-263-3886

Pronouns: she/her/hers

Fields: Labor Economics

Website


Rebecca Glawtschew
Position title:Lecturer

Email:rebecca.glawtschew@wisc.edu

Phone:608-890-2498

Pronouns: she/her/hers

Gregory, Jesse
Jesse Gregory
Position title:Director of Graduate Studies; Associate Professor

Email:jmgregory@ssc.wisc.edu

Phone:608-890-4913

Pronouns: he/him/his

Fields: Labor Economics, Public Economics

Website


Agustin Gutierrez
Position title:Assistant Professor

Email:gutierrez25@wisc.edu

Phone:608-263-4201

Fields: International trade, Macroeconomics, Labor

Website

Hansen, Bruce
Bruce Hansen
Position title:Professor, Mary Claire Aschenbrener Phipps Distinguished Chair

Email:bruce.hansen@wisc.edu

Phone:608-263-3880

Pronouns: he/him/his

Fields: Econometrics

Website

Hansen, David
David Hansen
Position title:Lecturer

Email:drhansen3@wisc.edu

Phone:608-265-8019

Pronouns: he/him/his

Fields: Development Economics and Labor Economics

Hansen, Korinna
Korinna Hansen
Position title:Senior Lecturer

Email:kohansen@ssc.wisc.edu

Phone:608-262-6853

Pronouns: she/her/hers

Fields: Applied Microeconomics, Health Economics

Website

Ken Hendricks
Kenneth Hendricks
Position title:Professor, Laurits R. Christensen Distinguished Chair

Email:hendrick@ssc.wisc.edu

Phone:608-263-3869

Fields: Industrial Organization

Website


Jean-Francois Houde
Position title:David Edwin and Lucille Hartmann Davies Chair in Economics

Email:houde@wisc.edu

Phone:608- 262-7927

Pronouns: he/him/his

Website

Johnson, David
David Johnson
Position title:Senior Lecturer

Email:djohnson64@wisc.edu

Phone:608-890-4912

Pronouns: he/him/his


Karam Kang
Position title:Associate Professor, Laurits R. Christensen Professorship in Economics

Email:kkang57@wisc.edu

Phone:608-265-6258

Pronouns: she/her/hers

Fields: Political Economy, Industrial Organization, Environmental Economics

Website

Placeholder headshot
John Kennan
Position title:Placement Director; Professor, Juli Plant Grainger Distinguished Chair

Email:jkennan@ssc.wisc.edu

Phone:608-262-5393

Fields: Labor Economics

Website


Rishabh Kirpalani
Position title:Associate Professor

Email:rishabh.kirpalani@wisc.edu

Phone:608-890-1289

Pronouns: he/him/his

Fields: Macroeconomics, Public Finance, International Economics, Financial Economics

Website

Lentz, Rasmus
Rasmus Lentz
Position title:Richard A. and Susan B. Strait Professor

Email:rlentz@ssc.wisc.edu

Phone:608-262-5373

Pronouns: he/him/his

Fields: Labor Economics, Macroeconomics, Microeconomics

Website

Magnolfi, Lorenzo
Lorenzo Magnolfi
Position title:Assistant Professor

Email:magnolfi@wisc.edu

Phone:608-262-8789

Fields: Industrial Organization, Applied Microeconomics, Applied Econometrics

Website

Christopher McKelvey
Christopher McKelvey
Position title:Lecturer

Email:cmckelvey@wisc.edu

Phone:608-263-7397

Pronouns: he/him/his

Fields: Development Economics

Website

Mommaerts, Corina
Corina Mommaerts
Position title:Associate Professor

Email:cmommaerts@wisc.edu

Phone:608-263-3213

Pronouns: she/her/hers

Fields: Public Economics, Labor Economics

Website


Martin O'Connell
Position title:Assistant Professor

Email:moconnell9@wisc.edu

Pronouns:  he/him/his

Fields: Public Economics, Industrial Organization

Website


Gregory Pac
Position title:Senior Lecturer

Email:gpac@wisc.edu

Phone:608-263-2287

Porter, Jack
Jack Porter
Position title:Professor, Richard E. Stockwell Distinguished Chair

Email:jrporter@ssc.wisc.edu

Phone:608-263-3870

Pronouns: he/him/his

Fields: Econometrics

Website

dan quint
Daniel Quint
Position title:Associate Professor

Email:dquint@ssc.wisc.edu

Phone:608-263-2515

Fields: Microeconomic Theory, Industrial Organization

Website

Rick, Steve
Steven Rick
Position title:Senior Lecturer

Email:steve.rick@cunamutual.com

Phone:608-262-0235


Fernanda Rojas-Ampuero
Position title:Assistant Professor

Email:rojasampuero@wisc.edu

Phone:608-265-8810

Pronouns: she/her/hers

Fields: Labor, Public, and Development Economics

Website

Rostek, Marzena
Marzena Rostek
Position title:Professor, Juli Plant Grainger Distinguished Chair

Email:mrostek@ssc.wisc.edu

Phone:608-262-6723

Pronouns: she/her/hers

Fields: Microeconomic Theory, Market Design, Finance

Website


Kim Ruhl
Position title:Curt and Sue Culver Professor of Economics; Co-Director, Center for Research on the Wisconsin Economy (CROWE)

Email:ruhl2@wisc.edu

Phone:608-263-3877

Pronouns: he/him/his

Field: International Economics

Website


Laura Schechter
Position title:Vilas Distinguished Achievement Professor

Email:lschechter@wisc.edu

Phone:608-262-9482

Fields: Development Economics, Behavioral and Experimental Economics

Website

Ananth Seshadri
Ananth Seshadri
Position title:Director of the Master’s Program, Professor, Mary Sue & Mike Shannon Distinguished Chair; Co-Director, Center for Research on the Wisconsin Economy (CROWE)

Email:aseshadr@ssc.wisc.edu

Phone:608-262-6196

Fields: Macroeconomics, Public Finance

Website

Shi, Xiaoxia
Xiaoxia Shi
Position title:Professor, Lowell and Leila Robinson Chair

Email:xshi@ssc.wisc.edu

Phone:608-262-8910

Pronouns: she/her/hers

Fields: Econometrics

Website


Jeffrey Smith
Position title:Professor, Paul T. Heyne Distinguished Chair in Economics; Richard A. Meese Chair in Applied Econometrics

Email:econjeff@ssc.wisc.edu

Phone:608-262-3066

Pronouns: he/him/his

Fields: Labor Economics, Public Economics

Website

lones smith
Lones Smith
Position title:Professor, Maude P. & Milton J. Shoemaker Distinguished Chair; David Blackwell Professor of Economics

Email:lones@ssc.wisc.edu

Phone:608-263-3871

Fields: Microeconomic Theory

Website


Alan Sorensen
Position title:Professor, John and Tashia Morgridge Chair

Email:sorensen@ssc.wisc.edu

Phone:608-263-3867

Pronouns: he/him/his

Fields: Industrial Organization

Website

Sullivan, Christopher
Christopher Sullivan
Position title:Assistant Professor

Email:cjsullivan@wisc.edu

Phone:608-263-3861

Pronouns: he/him/his

Fields: Industrial Organization, Applied Microeconomics

Website


Ashley Swanson
Position title:Associate Professor, Douglas W. and Sherry A. Caves Professor of Economics

Email:swanson25@wisc.edu

Phone:608-262-5897

Pronouns: she/her/hers

Fields: Industrial Organization, Health Economics, Education

Website


Christopher Taber
Position title:Department Chair; James J. Heckman Professor; Walker Family Distinguished Chair

Email:ctaber@ssc.wisc.edu

Phone:608-263-7791

Pronouns: he/him/his

Fields: Labor Economics, Applied Econometrics, Public Economics

Website


Steve Trost
Position title:Lecturer

Email:strost2@wisc.edu

Phone:608-262-6794

Pronouns: he/him/his

Website

Weretka, Marek
Marek Weretka
Position title:Stuart & Brenda McCroskey Professor of Economics

Email:mweretka@ssc.wisc.edu

Phone:608-262-2265

Fields: Economic Theory, Finance

Website

ken west
Kenneth West
Position title:John D. MacArthur Professor

Email:kdwest@wisc.edu

Phone:608-262-0033

Pronouns: he/him/his

Fields: Macroeconomics, Econometrics

Website

Randall Wright
Randall Wright
Position title:Ray Zemon Professor of Liquid Assets

Email:randall.wright@wisc.edu

Phone:608-262-9890

Fields: Macroeconomics, Finance

Website


Alice Wu
Position title:Postdoctoral Fellow

Email:hwu526@wisc.edu

Phone:608-265-7473

Fields: Labor, Personnel, Innovation

Website


Kohei Yata
Position title:Assistant Professor

Email:yata@wisc.edu

Fields: Econometric Theory, Applied Econometrics

Website

Site footer content
Part of the Universities of Wisconsin
Site Links
Undergraduate Program
Master’s Program
Doctoral Program
Alumni
Events
Faculty
Contact Us
Department of Economics
William H. Sewell Social Science Building
1180 Observatory Drive
Madison, WI 53706-1393
Map
Phone: 608-263-2989
Website feedback, questions or accessibility issues: tninmann@wisc.edu | Learn more about accessibility at UW–Madison.

This site was built using the UW Theme | Privacy Notice | © 2024 Board of Regents of the University of Wisconsin System.

Cookie Notice
We use cookies on this site. By continuing to browse without changing your browser settings to block or delete cookies, you agree to the UW–Madison Cookie Notice.
Accept cookie notice
Skip to main content
University of Wisconsin–Madison
Computer Sciences
School of Computer, Data & Information Sciences
Search
Search
Home
Undergraduate
Graduate
The Student Experience
Courses
Research
People
Careers
Make a Gift
MyCompSci
The Wisconsin Computing Idea
Faculty
Faculty

Ali Abedi
Position title:Assistant Professor

Email:aabedi@wisc.edu

Phone:Computer Sciences 6355

Aws Albarghouthi headshot
Aws Albarghouthi
Position title:Associate Professor

Email:aws@cs.wisc.edu

Phone:608-262-7946

Address:
6363 Computer Sciences

Andrea Arpaci-Dusseau headshot
Andrea Arpaci-Dusseau
Position title:Catherine A. Erickson Professor; Susan B. Horwitz Professor

Email:dusseau@cs.wisc.edu

Phone:608-265-6013

Address:
7375 Computer Sciences


Remzi Arpaci-Dusseau
Position title:Grace Wahba Professor; Vilas Distinguished Achievement Professor

Email:remzi@cs.wisc.edu

Phone:608-263-7764

Address:
7357 Computer Sciences

Eric Bach headshot
Eric Bach
Position title:Professor

Email:bach@cs.wisc.edu

Phone:608-262-7997

Address:
4391 Computer Sciences

Suman Banerjee headshot
Suman Banerjee
Position title:David J. DeWitt Professor and Associate Chair for Professional Programs

Email:suman@cs.wisc.edu

Phone:608-262-7387

Address:
7391 Computer Sciences

Paul Barford headshot
Paul Barford
Position title:Professor and Associate Chair for Faculty Affairs

Email:pb@cs.wisc.edu

Phone:608-262-6609

Address:
7393 Computer Sciences

Jin-Yi Cai headshot
Jin-Yi Cai
Position title:Steenbock Professor

Email:jyc@cs.wisc.edu

Phone:608-262-3158

Address:
4393 Computer Sciences

Ethan Cecchetti
Ethan Cecchetti
Position title:Assistant Professor

Email:cecchetti@wisc.edu

Address:
7395 Computer Sciences


Tej Chajed
Position title:Assistant Professor

Email:chajed@wisc.edu

Address:
7361 Computer Sciences


Rahul Chatterjee
Position title:Assistant Professor

Email:rahul.chatterjee@wisc.edu

Phone:608-262-5306

Address:
7373 Computer Sciences


Yudong Chen
Position title:Associate Professor

Email:yudong.chen@wisc.edu

Address:
5373 Computer Sciences

Ilias Diakonikolas headshot
Ilias Diakonikolas
Position title:Sheldon B. Lubar Professor

Email:ilias@cs.wisc.edu

Phone:608-262-4694

Address:
4387 Computer Sciences

Jelena Diakonikolas headshot
Jelena Diakonikolas
Position title:Assistant Professor

Email:jdiakonikola@wisc.edu

Address:
4369 Computer Sciences

Anhai Doan headshot
AnHai Doan
Position title:Vilas Distinguished Achievement Professor; Gurindar S. Sohi Professor

Email:anhai@cs.wisc.edu

Phone:608-262-9759

Address:
4355 Computer Sciences

Michael Ferris headshot
Michael Ferris
Position title:John P. Morgridge Chair; Jacques-Louis Lions Professor

Email:ferris@cs.wisc.edu

Phone:608-262-4281

Address:
4381 Computer Sciences

Michael Gleicher headshot
Michael Gleicher
Position title:Professor

Email:gleicher@cs.wisc.edu

Phone:608-263-2874

Address:
6385 Computer Sciences


Rishab Goyal
Position title:Assistant Professor

Email:rishab.goyal@wisc.edu

Address:
4373 Computer Sciences

Mohit Gupta headshot
Mohit Gupta
Position title:Associate Professor

Email:mohitg@cs.wisc.edu

Phone:608-890-0124

Address:
6395 Computer Sciences


Josiah Hanna
Position title:Assistant Professor

Email:jphanna@cs.wisc.edu

Address:
5391 Computer Sciences


Charles Lee Isbell, Jr.
Position title:Hilldale Professor and UW-Madison Provost

Email:provost@provost.wisc.edu

Phone:608-262-1304

Somesh Jha headshot
Somesh Jha
Position title:Sheldon B. Lubar Chair and Professor

Email:jha@cs.wisc.edu

Phone:608-262-9519

Address:
7385 Computer Sciences


Kirthevasan (Kirthi) Kandasamy
Position title:Assistant Professor

Email:kandasamy@cs.wisc.edu

Address:
5375 Computer Sciences

Paris Koutris headshot
Paris Koutris
Position title:Associate Professor

Email:paris@cs.wisc.edu

Phone:608-263-1965

Address:
4363 Computer Sciences


Yong Jae Lee
Position title:Associate Professor

Email:yongjaelee@cs.wisc.edu

Address:
5395 Computer Sciences


Sharon Li
Position title:Assistant Professor

Email:sharonli@cs.wisc.edu

Address:
5393 Computer Sciences

Yingyu Liang headshot
Yingyu Liang
Position title:Associate Professor

Email:yliang@cs.wisc.edu

Phone:608-262-7784

Address:
6393 Computer Sciences

Ming Liu headshot
Ming Liu
Position title:Assistant Professor

Email:mgliu@cs.wisc.edu

Address:
7379 Computer Sciences

Miron Livny Headshot
Miron Livny
Position title:John P. Morgridge Chair; Vilas Research Professor

Email:miron@cs.wisc.edu

Phone:608-262-0856

Address:
4367 Computer Sciences


Patrick McDaniel
Position title:Tsun-Ming Shih Professor

Email:pdmcdaniel@wisc.edu

Address:
7387 Computer Sciences

Dieter van Melkebeek headshot
Dieter van Melkebeek
Position title:Professor

Email:dieter@cs.wisc.edu

Phone:608-262-4196

Address:
4390 Computer Sciences

Barton Miller headshot
Barton Miller
Position title:Vilas Distinguished Achievement Professor; Amar & Balinder Sohi Professor

Email:bart@cs.wisc.edu

Phone:608-263-3378


Bilge Mutlu
Position title:Sheldon B. and Marianne S. Lubar Professor

Email:bilge@cs.wisc.edu

Phone:608-262-6635

Address:
6381 Computer Sciences

Thomas Reps headshot
Thomas Reps
Position title:J. Barkley Rosser Professor; Rajiv and Ritu Batra Chair

Email:reps@cs.wisc.edu

Phone:608-262-2091

Address:
6361 Computer Sciences

Amos Ron headshot
Amos Ron
Position title:Professor

Email:amos@cs.wisc.edu

Phone:608-262-6621

Address:
7381 Computer Sciences

Frederic Sala
Frederic Sala
Position title:Assistant Professor

Email:fredsala@cs.wisc.edu

Address:
5385 Computer Sciences

Karu Sankaralingam headshot
Karthikeyan Sankaralingam
Position title:Mark D. Hill and David A. Wood Professor and Associate Chair for Instruction

Email:karu@cs.wisc.edu

Phone:608-890-0121

Address:
6367 Computer Sciences

Eftychios Sifakis headshot
Eftychios Sifakis
Position title:Professor and Associate Chair for Graduate Studies

Email:sifakis@cs.wisc.edu

Phone:608-262-5083

Address:
6387 Computer Sciences


Sandeep Silwal
Position title:Assistant Professor

Email:silwal@cs.wisc.edu

Address:
4351 Computer Sciences

Matt Sinclair headshot
Matthew Sinclair
Position title:Assistant Professor

Email:sinclair@cs.wisc.edu

Phone:608-263-7463

Address:
6369 Computer Sciences

Gurindar Sohi headshot
Gurindar Sohi
Position title:E. David Cronon Professor; Vilas Research Professor

Email:sohi@cs.wisc.edu

Phone:608-262-7985

Address:
6375 Computer Sciences

Michael Swift headshot
Michael Swift
Position title:Vilas Distinguished Achievement Professor

Email:swift@cs.wisc.edu

Phone:608-890-0131

Address:
7369 Computer Sciences


Swamit Tannu
Position title:Assistant Professor

Email:stannu@wisc.edu

Address:
6373 Computer Sciences

Shivaram Venkataraman headshot
Shivaram Venkataraman
Position title:Assistant Professor

Email:shivaram@cs.wisc.edu

Address:
7367 Computer Sciences


Manolis Vlatakis
Position title:Assistant Professor

Email:vlatakis@wisc.edu


Stephen Wright
Position title:Department Chair; George B. Dantzig Professor; Sheldon B. Lubar Chair; Hilldale Professor

Email:swright@cs.wisc.edu

Phone:608-262-4838

Address:
4379 Computer Sciences


Tengyang Xie
Position title:Assistant Professor

Email:tx@cs.wisc.edu

Xiangyao Yu
Xiangyao Yu
Position title:Assistant Professor

Email:yxy@cs.wisc.edu

Address:
4385 Computer Sciences

Yuhang Zhao
Yuhang Zhao
Position title:Assistant Professor

Email:yuhang.zhao@cs.wisc.edu

Address:
Computer Sciences 6393


Jerry Zhu
Position title:Stephen Kleene Professor

Email:jerryzhu@cs.wisc.edu

Phone:608-890-0129

Address:
6391 Computer Sciences

Teaching Faculty

Mouna Ayari Ben Hadj Kacem
Position title:Faculty Associate

Email:mouna@cs.wisc.edu

Tyler Caraza-Harter
Tyler Caraza-Harter
Position title:Faculty Associate

Email:harter@cs.wisc.edu

Gary Dahl
Gary Dahl
Position title:Faculty Associate

Email:dahl@cs.wisc.edu

Phone:608-262-9415

Address:
4395 Computer Sciences

Deb Deppeler
Deb Deppeler
Position title:Faculty Associate

Email:deppeler@cs.wisc.edu

Phone:608-265-9452

Address:
5376 Computer Sciences


Michael Doescher
Position title:Faculty Associate

Email:doescher@cs.wisc.edu


Blerina Gkotse
Position title:Faculty Associate

Email:gkotse@wisc.edu

Beck Hasti
Beck Hasti
Position title:Faculty Associate

Email:hasti@cs.wisc.edu

Phone:608-263-2622

Address:
5375 Computer Sciences


Florian Heimerl
Position title:Faculty Associate

Email:heimerl@cs.wisc.edu


Andrew Kuemmel
Position title:WES-CS Program Director

Email:kuemmel@cs.wisc.edu

Hobbes LeGault
L. Hobbes Legault
Position title:Faculty Associate

Email:legault@wisc.edu

Address:
5388 Computer Sciences


Hina Mahmood
Position title:Faculty Associate

Email:mahmood@cs.wisc.edu


Cole Nelson
Position title:Faculty Associate

Email:ctnelson2@wisc.edu


Louis Oliphant
Position title:Faculty Associate

Email:ltoliphant@wisc.edu


Kaiser Pister
Position title:Faculty Associate

Email:kaiser@cs.wisc.edu


Marc Renault
Position title:Faculty Associate

Email:mrenault@cs.wisc.edu


Gurmail Singh
Position title:Faculty Associate

Email:gurmail.singh@wisc.edu


James Skrentny
Position title:Faculty Associate

Email:skrentny@cs.wisc.edu

Phone:608-262-0191

Address:
4378 Computer Sciences


Scott Swanson
Position title:Faculty Associate

Email:scott.swanson@wisc.edu


Meenakshi Syamkumar
Position title:Faculty Associate

Email:ms@cs.wisc.edu


Jim Williams
Position title:Faculty Associate

Email:jimw@cs.wisc.edu

Phone:608-262-6181

Address:
6384 Computer Sciences


Young Wu
Position title:Faculty Associate

Email:yw@cs.wisc.edu

Instructors

Kristin Brown
Position title:CS 402 instructor

Email:kmbrown26@wisc.edu


Amber Field
Position title:Instructional Administrator

Email:afield@wisc.edu

Affiliate Faculty
Joe Austerweil headshot
Joseph Austerweil
Position title:Assistant Professor, Department of Psychology

Email:austerweil@wisc.edu

Phone:608-262-9932


Juan Caicedo
Position title:Assistant Professor, Biostatistics & Medical Informatics

Email:juan.caicedo@wisc.edu


Kyle Cranmer
Position title:Professor, Physics Department; Director, American Family Data Science Institute

Mark Craven headshot
Mark Craven
Position title:Professor, Department of Biostatistics & Medical Informatics

Email:craven@biostat.wisc.edu

Alberto Del Pia headshot
Alberto Del Pia
Position title:Associate Professor, College of Engineering

Email:delpia@wisc.edu

Colin Dewey headshot
Colin Dewey
Position title:Professor, Biostatistics & Medical Informatics

Email:cdewey@cs.wisc.edu

Phone:608-263-7610

Kassem Fawaz headshot
Kassem Fawaz
Position title:Assistant Professor, Electrical & Computer Engineering

Email:kfawaz@wisc.edu

Phone:608-890-0529

Anthony Gitter headshot
Anthony Gitter
Position title:Assistant Professor, Biostatistics & Medical Informatics

Email:gitter@biostat.wisc.edu

Phone:608-316-4442

Junhie Hu
Junjie Hu
Position title:Assistant Professor, Department of Biostatistics & Medical Informatics

Email:junjie.hu@wisc.edu


Tsung-Wei Huang
Position title:Assistant Professor, Electrical & Computer Engineering

Email:tsung-wei.huang@wisc.edu


Bhuvana Krishnaswamy
Position title:Assistant Professor, Electrical & Computer Engineering

Email:bhuvana@ece.wisc.edu

Phone:(608) 265-7849

Kangwook Lee
Kangwook Lee
Position title:Assistant Professor, Electrical & Computer Engineering

Email:kangwook.lee@wisc.edu

Phone:608-265-4841


Benjamin Lengerich
Position title:Assistant Professor, Department of Statistics

Email:lengerich@wisc.edu

Yin Li headshot
Yin Li
Position title:Assistant Professor, Department of Biostatistics & Medical Informatics

Email:yin.li@wisc.edu

Jeffrey Linderoth headshot
Jeffrey Linderoth
Position title:Professor, Industrial & Systems Engineering

Email:linderoth@wisc.edu

Mikko Lipasti headshot
Mikko Lipasti
Position title:Professor, Electrical & Computer Engineering

Email:mikko@engr.wisc.edu

Phone:608-265-2639

James Luedtke headshot
James Luedtke
Position title:Associate Professor, Industrial & Systems Engineering

Email:jim.luedtke@wisc.edu


Pedro Morgado
Position title:Assistant Professor, Electrical & Computer Engineering

Email:pmorgado@wisc.edu

Dan Negrut headshot
Dan Negrut
Position title:Professor, Mechanical Engineering

Email:negrut@wisc.edu

Robert Nowak headshot
Robert Nowak
Position title:Professor, Electrical & Computer Engineering

Email:rdnowak@wisc.edu


Irene Ong
Position title:Associate Professor, Obstetrics & Gynecology, Biostatistics & Medical Informatics

Email:ong@biostat.wisc.edu

Dimitris Papailiopoulos headshot
Dimitris Papailiopoulos
Position title:Assistant Professor, Electrical & Computer Engineering

Email:dimitris@ece.wisc.edu

Kevin Ponto headshot
Kevin Ponto
Position title:Associate Professor, Design Studies, School of Human Ecology

Email:kponto@cs.wisc.edu

Parameswaran Ramanathan headshot
Parameswaran Ramanathan
Position title:Professor, Electrical & Computer Engineering

Email:parmesh@cs.wisc.edu

Phone:608-263-0557

Sushmita Roy headshot
Sushmita Roy
Position title:Associate Professor, Biostatistics & Medical Informatics

Email:sroy@cs.wisc.edu


Maja Rudolph
Position title:Research Professor. Data Science Institute

Email:maja.rudolph@wisc.edu

Joshua San Miguel headshot
Joshua San Miguel
Position title:Assistant Professor, Electrical & Computer Engineering

Email:jsanmiguel@cs.wisc.edu

Phone:608-890-2635

Vadim Shapiro headshot
Vadim Shapiro
Position title:Professor, Mechanical Engineering

Email:shapiro@cs.wisc.edu

Phone:608-262-3591

Vikas Singh headshot
Vikas Singh
Position title:Professor, Department of Biostatistics & Medical Informatics

Email:vsingh@cs.wisc.edu

Phone:608-262-8875


Jacob Thebault-Spieker
Position title:Assistant Professor, The Information School

Email:jacob.thebaultspieker@wisc.edu

Ramya Vinayak headshot
Ramya Vinayak
Position title:Assistant Professor, Electrical & Computer Engineering

Email:ramya@ece.wisc.edu

Daifeng Wang
Daifeng Wang
Position title:Assistant Professor, Biostatistics & Medical Informatics

Email:daifeng.wang@wisc.edu


Chaowei Xiao
Position title:Assistant Professor, the Information School

Email:cxiao34@wisc.edu


Qiaomin Xie
Position title:Assistant Professor, Industrial and Systems Engineering

Email:qiaomin.xie@wisc.edu

Emeritus Faculty
Carl de Boor
Carl de Boor
Position title:Emeritus

Email:deboor@cs.wisc.edu

David DeWitt
David DeWitt
Position title:Emeritus

Email:david.dewitt@outlook.com

Charles Dyer headshot
Charles Dyer
Position title:Emeritus

Email:dyer@cs.wisc.edu

Charles Fischer headshot
Charles Fischer
Position title:Emeritus

Email:fischer@cs.wisc.edu

James Goodman
James Goodman
Position title:Emeritus

Email:goodman@cs.wisc.edu

Mark Hill headshot
Mark D. Hill
Position title:Emeritus

Email:markhill@cs.wisc.edu

Deborah Joseph headshot
Deborah Joseph
Email:joseph@cs.wisc.edu

Phone:608-262-8022

Lawrence Landweber headshot
Lawrence Landweber
Position title:Emeritus

Email:lhl@cs.wisc.edu

Robert R. Meyer
Robert Meyer
Position title:Emeritus

Email:rrm@cs.wisc.edu

Jeffrey Naugton
Jeffrey Naughton
Position title:Emeritus

Email:naughton@cs.wisc.edu


Seymour Parter
Position title:Emeritus

Email:parter@cs.wisc.edu

Stephen Robinson headshot
Stephen Robinson
Position title:Emeritus

Email:smr@cs.wisc.edu

Jude Shavlik headshot
Jude Shavlik
Position title:Emeritus

Email:shavlik@cs.wisc.edu


Marvin Solomon
Position title:Emeritus

Email:solomon@cs.wisc.edu


John Strikwerda
Position title:Emeritus

Email:strik@cs.wisc.edu


Mary Vernon
Position title:Emeritus

Email:vernon@cs.wisc.edu

Grace Wahba headshot
Grace Wahba
Position title:Professor Emeritus, Department of Statistics, Computer Sciences Affiliate Faculty

Email:wahba@cs.wisc.edu

Phone:608-262-3620


David Wood
Position title:Emeritus

Email:david@cs.wisc.edu

In Memoriam
We celebrate faculty members we have lost at the link below.

In memoriam

Site footer content
Part of the Universities of Wisconsin
Quick Links
Comp Sci Courses
Industrial Affiliates Program
IT Services
Make a Gift
Email Contacts
CS Undergraduate Advising – current students
CS Prospective Undergraduates
UW-Madison Undergrad Admissions
Undergrad International Admissions
CS Graduate Admissions Emails
CS MS/PhD Coordinator
CS PMP/Capstone Coordinator
Other CS Contacts
Contact Us
1210 W. Dayton Street
Madison, WI 53706-1613
Map
Phone: 608-262-1204
Website feedback, questions or accessibility issues: feedback@cs.wisc.edu | Learn more about accessibility at UW–Madison.

This site was built using the UW Theme | Privacy Notice | © 2024 Board of Regents of the University of Wisconsin System.

Cookie Notice
We use cookies on this site. By continuing to browse without changing your browser settings to block or delete cookies, you agree to the UW–Madison Cookie Notice.
Accept cookie notice
Skip to main content
University of Wisconsin–Madison : physics
Department of Physics
Research, teaching and outreach in Physics at UW–Madison
Search
Search
Graduate
Undergraduate
Research
People
News & Events
Climate & Diversity
Outreach
Resources
Giving
Contact
Courses
Jobs
Visit
Log in
Home
People
Department Staff
Department Staff
Administrative Staff
Christine Adamavich
Position title:Curricular And Admin Assistant

Email:cadamavich@wisc.edu

Phone:(608) 262-4526

2320 Chamberlin Hall

Susan Anderson
Position title:Financial Specialist

Email:susan.anderson@wisc.edu

Photo of Evan Heintz
Evan Heintz
Position title:Undergraduate Advisor

Email:eheintz@wisc.edu

Phone:(608) 263-7450

2320 D Chamberlin Hall

profile photo of Sharon Kahn
Sharon Kahn
Position title:Graduate Program Manager, PhD Program

Email:smkahn@wisc.edu

Phone:(608) 262-9678

2320 F Chamberlin Hall

profile photo of sylvia Kmiec
Sylvia Swift Kmiec
Position title:Senior Research Administrator

Email:sylvia.kmiec@wisc.edu

Phone:(608) 262-4964

4278 Chamberlin Hall

Aimee Lefkow
Position title:Research Program Manager/Department Administrator

Email:lefkow@hep.wisc.edu

Phone:(608) 263-2267

4281 Chamberlin Hall

Donald L Miner
Position title:Travel Approver

Email:donminer@physics.wisc.edu

Phone:(608) 262-2281

4288 Chamberlin Hall

profile picture of Katerina Moloni
Katerina Moloni
Position title:Associate Director, MSPQC and WQI

Email:moloni@wisc.edu

5207 Chamberlin Hall

Photo of Samantha Robertson
Samantha Robertson
Position title:Procurement & Post Award

Email:sjrobertson2@wisc.edu

Phone:(608) 262-4826

4281 Chamberlin Hall

profile photo of Mae Saul
Mae Saul
Position title:Director of Development, Planned Giving, Fundraising

Email:mae.saul@supportuw.org

Phone:(608) 216-6274

Dawn M Suchomel
Position title:Travel & Events Coordinator

Email:dmsuchomel@wisc.edu

Phone:(608) 262-7782

4288 Chamberlin Hall

Helen Yangazova
Position title:Student Program Coordinator

Email:yangazova@wisc.edu

Phone:(608) 262-2281

2320 Chamberlin Hall


Rachel Zizmann
Position title:Diversity & Inclusion Coordinator

Email:rachel.zizmann@wisc.edu

Phone:(608) 262-2118

4211 Chamberlin Hall

Communications & Outreach Staff
profile photo of Cierra Atkinson
Cierra Atkinson
Position title:Outreach Program Manager

Email:catkinson5@wisc.edu

Phone:(608) 262-1137

1150 Chamberlin Hall

profile photo of Haddie McLean
Haddie McLean
Position title:Outreach Program Manager

Email:haddie@physics.wisc.edu

Phone:(608) 262-2927

1209 Chamberlin Hall

Photo of Sarah Parker
Sarah Parker
Position title:Quantum Outreach Program Manager

Email:sarah.parker@wisc.edu

1150 Chamberlin Hall

profile photo of Sarah Perdue
Sarah Perdue
Position title:Communications Manager

Email:saperdue@wisc.edu

Phone:(608) 262-3051

2320h Chamberlin Hall

Photo of Aubree Steinmetz
Aubree Steinmetz
Position title:Outreach Specialist

Email:aosteinmetz@wisc.edu

Instructional Staff
Photo of Alessandro Cunsolo
Alessandro Cunsolo
Position title:Teaching Faculty

Email:cunsolo@wisc.edu

Phone:(608) 263-2637

1336 Chamberlin Hall


Carrie Francis
Position title:Dir Of Intro & Service Courses

Email:cfrancis2@wisc.edu

Phone:(608) 262-8696

4211 Chamberlin Hall

profile photo of Mitch McNanna
Mitch McNanna
Position title:Teaching Specialist

Email:mcnanna@wisc.edu

6246 Chamberlin Hall

profile photo of Abdollah Mohammadi
Abdollah Mohammadi
Position title:Teaching Faculty

Email:mohammadi4@wisc.edu

3114 Chamberlin Hall

Steve R Narf
Position title:Lecture Demonstration

Email:srnarf@wisc.edu

Phone:(608) 262-3898

2237 Chamberlin Hall

Profile photo of Jim Reardon
Jim Reardon
Position title:Director of Undergraduate Program

Email:reardon@physics.wisc.edu

Phone:(608) 262-0945

2320g Chamberlin Hall

Jeffrey R Schmidt
Position title:Distinguished Teaching Faculty

Email:jrschmi2@wisc.edu

Phone:(608) 890-2004

5213 Chamberlin Hall

profile photo of benjamin spike
Benjamin Spike
Position title:Director of Active Learning

Email:btspike@wisc.edu

Phone:(608) 265-2052

3112 Chamberlin Hall

Daniel Patrick Thurs
Position title:Teaching Faculty

Email:dpthurs@wisc.edu

Phone:(608) 262-2356

3110 Chamberlin Hall

Brett Unks
Position title:Instructional Lab Manager

Email:unks@wisc.edu

Phone:(608) 262-0075

4120 Chamberlin Hall

profile photo of Josh Weber
Josh Weber
Position title:Teaching Faculty

Email:jjweber3@wisc.edu

Phone:(608) 265-6669

4122 Chamberlin Hall

IT / Computing
Photo of Dan Bradley
Dan Bradley
Position title:Director of Computing

Email:dan@physics.wisc.edu

3116 Chamberlin Hall


Chad W Seys
Position title:Computer Systems Administrator

Email:cwseys@physics.wisc.edu

Phone:(608) 262-0629

3118 Chamberlin Hall

Physics Learning Center

Eric Hooper
Position title:PLC Instructor

Email:ehooper@astro.wisc.edu

Phone:(608) 890-0767

2337 Chamberlin Hall

profile photo of Chris Moore
Chris Moore
Position title:PLC Instructor

Email:cmoore@physics.wisc.edu

Phone:(608) 890-0767

2337 Chamberlin Hall


Susan M Nossal
Position title:Senior Scientist/Director, Physics Learning Center

Email:nossal@physics.wisc.edu

Phone:(608) 262-9107

2334 A Chamberlin Hall

Melissa Sikes
Melissa M Sikes
Position title:PLC Instructor

Email:mmsikes@wisc.edu

Phone:(608) 890-0767

2337 Chamberlin Hall


Akire Trestrail
Position title:PLC Teaching Assistant

Email:trestrail@wisc.edu

2338 Chamberlin Hall

Instrumentation and Electronics
Jay S Bowe
Position title:Physics Instrument Shop Mgr

Email:jsbowe@wisc.edu

Phone:(608) 262-7380

1228 Chamberlin Hall

William B Foster
Position title:Instrument Maker

Email:wbfoster@wisc.edu

Phone:(608) 262-7380

1228 Chamberlin Hall

Billy James Gates
Position title:Electronics Shop Technologist

Email:bjgates@wisc.edu

Phone:(608) 262-0527

3336 Chamberlin Hall

Daniel Patrick Pape
Position title:Instrument Maker

Email:dpape2@wisc.edu

Phone:(608) 262-7380

1228 Chamberlin Hall

Craig Stiemke
Position title:Instrument Maker

Email:castiemke@wisc.edu

Phone:(608) 262-7380

1228 Chamberlin Hall

Sara K Yaeger
Position title:Instrument Maker

Email:skyaeger@wisc.edu

Phone:(608) 262-3998

1228 Chamberlin Hall

Site footer content
Part of the Universities of Wisconsin
Contact Us
Physics Department
2320 Chamberlin Hall
1150 University Avenue
Madison, WI 53706-1390
Map
Email: info@physics.wisc.edu
Phone: 608-262-4526
Website feedback, questions or accessibility issues: it-staff@physics.wisc.edu.

Learn more about accessibility at UW–Madison.

This site was built using the UW Theme | Privacy Notice | © 2024 Board of Regents of the University of Wisconsin System.

Cookie Notice
We use cookies on this site. By continuing to browse without changing your browser settings to block or delete cookies, you agree to the UW–Madison Cookie Notice.
Accept cookie notice
Skip to main content
University of Wisconsin–Madison
Department of Chemistry
College of Letters & Science
Search
Search
People
Academics
Research
Seminars & Events
Facilities & Services
Outreach
Safety
About
Home
Alumni & Friends
Community
Give
Intranet
MyUW
Wellness
Home
Faculty
Faculty
All Faculty  |  Analytical  |  Chemical Biology  |  Chemistry Education  |  Inorganic  |  Materials  |  Organic  |  Physical  |  Theoretical/Computational

Affiliate Faculty  |  Emeriti Faculty

Chemistry Faculty
John Berry
Berry, John F.
Position title:Lester R. McNall Professor of Chemistry

Email:berry@chem.wisc.edu

Phone:608.262.7534

Tim Bertram
Bertram, Tim
Position title:Professor of Chemistry, Affiliate Professor of Atmospheric and Oceanic Sciences

Email:tbertram@chem.wisc.edu

Phone:608.890.3422


Blackwell, Helen
Position title:Norman C. Craig Professor of Chemistry

Email:blackwell@chem.wisc.edu

Phone:608.262.1503


Boros, Eszter
Credentials:Hall-Fisher Associate Professor of Chemistry, Affiliate Professor for the Department of Medical Physics, School of Medicine and Public Health

Position title:Associate Professor

Email:eboros@wisc.edu

AJ Boydston
Boydston, AJ
Position title:Professor of Chemistry, Yamamoto Family Professor, Affiliate in MSE and CBE

Email:aboydston@wisc.edu

Thomas Brunold
Brunold, Thomas
Position title:Professor of Chemistry

Email:brunold@chem.wisc.edu

Phone:608.265.9056

Andrew Buller
Buller, Andrew R.
Position title:Associate Professor of Chemistry

Email:arbuller@wisc.edu

Phone:608.265.8431

Judith Burstyn
Burstyn, Judith N.
Position title:Professor of Chemistry

Email:burstyn@chem.wisc.edu

Phone:608.262.0328

Silvia Cavagnero
Cavagnero, Silvia
Position title:Professor of Chemistry

Email:cavagnero@chem.wisc.edu

Phone:608.262.5430

Choi
Choi, Kyoung-Shin
Position title:Professor of Chemistry

Email:kschoi@chem.wisc.edu

Phone:608.262.5859

Joshua Coon
Coon, Joshua J.
Position title:Professor of Biomolecular Chemistry and Chemistry

Email:jcoon@chem.wisc.edu

Phone:608.263.1718


Cooper, Julian
Position title:Assistant Professor

Email:jccooper5@wisc.edu

Mark Ediger
Ediger, Mark D.
Position title:Hyuk Yu Professor of Chemistry

Email:ediger@chem.wisc.edu

Phone:608.262.7273

Daniel Fredrickson
Fredrickson, Daniel C.
Position title:Professor of Chemistry

Email:danny@chem.wisc.edu

Phone:608.890.1567

Etienne Garand
Garand, Etienne
Position title:Professor of Chemistry

Email:egarand@chem.wisc.edu

Phone:608.890.4905

Sam Gellman
Gellman, Samuel H.
Position title:Irving Shain Chair of Chemistry, Professor of Chemistry, Vilas Research Professor, Ralph F. Hirschmann Professor of Chemistry

Email:gellman@chem.wisc.edu

Phone:608.262.3303

Randall Goldsmith
Goldsmith, Randall
Position title:Professor of Chemistry

Email:rhg@chem.wisc.edu

Phone:608.263.8315

Bob Hamers
Hamers, Robert J.
Position title:Professor of Chemistry, Steenbock Professor of Physical Science

Email:rjhamers@wisc.edu

Phone:608.262.6371

Ive Hermans
Hermans, Ive
Position title:John and Dorothy Vozza Professor of Chemistry, Professor of Chemical and Biological Engineering

Email:hermans@chem.wisc.edu

Phone:608.262.4966

Person with glasses smiling
Huang, Xuhui
Credentials:Director, Theoretical Chemistry Institute

Position title:Hirschfelder Chair in Theoretical Chemistry, Professor of Chemistry

Email:xhuang448@wisc.edu

Song Jin
Jin, Song
Position title:Francis J. DiSalvo Professor of Physical Science

Email:jin@chem.wisc.edu

Phone:608.262.1562

Clark Landis
Landis, Clark
Position title:Professor of Chemistry

Email:landis@chem.wisc.edu

Phone:608.262.0362

Jeff Martell
Martell, Jeff
Position title:Assistant Professor of Chemistry

Email:jdmartell@wisc.edu

Phone:608.263.6249

Robert McMahon
McMahon, Robert J.
Position title:Professor of Chemistry

Email:robert.mcmahon@wisc.edu

Phone:608.262.0660


Nathanson, Gilbert
Position title:Professor of Chemistry

Email:nathanson@chem.wisc.edu

Phone:608.262.8098

Sam Pazicni
Pazicni, Sam
Position title:Assistant Professor of Chemistry

Email:sam.pazicni@chem.wisc.edu

Phone:608.263.5801

JR Schmidt
Schmidt, JR
Position title:Professor of Chemistry, Associate Chair for the Undergraduate Program

Email:schmidt@chem.wisc.edu

Phone:608.262.2996

Jennifer Schomaker
Schomaker, Jennifer
Position title:Professor of Chemistry

Email:schomakerj@chem.wisc.edu

Phone:608.265.2261

David Schwartz
Schwartz, David C.
Position title:Kellett Professor of Chemistry and Genetics

Email:schwartz@chem.wisc.edu

Phone:608.265.0546

Lloyd Smith
Smith, Lloyd M.
Position title:W. L. Hubbell Professor of Chemistry, Hall-Fischer Professor of Chemistry

Email:smith@chem.wisc.edu

Phone:608.263.2594


Soley, Micheline
Position title:Assistant Professor of Chemistry

Email:msoley@wisc.edu

Phone:608.262.0263

Shannon Stahl
Stahl, Shannon
Position title:Professor of Chemistry, Steenbock Professor of Chemical Sciences

Email:stahl@chem.wisc.edu

Phone:608.265.6288

Ryan Stowe
Stowe, Ryan
Position title:Assistant Professor of Chemistry

Email:rstowe@chem.wisc.edu

Phone:608.890.2568


Todd, Zoe
Position title:Assistant Professor

Email:zrtodd@wisc.edu

Tina Wang
Wang, Tina
Position title:Assistant Professor of Chemistry

Email:twang495@wisc.edu

Phone:608.263.5807

Dan Weix
Weix, Daniel
Position title:Wayland E. Noland Distinguished Professor of Chemistry

Email:dweix@wisc.edu

Phone:608.262.0541

Zach Wickens
Wickens, Zach
Position title:Associate Professor of Chemistry

Email:wickens@wisc.edu

Phone:608.890.4906


Widicus Weaver, Susanna
Position title:Vozza Professor of Chemistry and Astronomy

Email:slww@chem.wisc.edu

Yang Yang
Yang, Yang
Position title:Assistant Professor of Chemistry

Email:yyang222@wisc.edu

Phone:608.262.9801

Arun Yethiraj
Yethiraj, Arun
Position title:V. W. Meloche-Bascom Professor of Chemistry

Email:yethiraj@chem.wisc.edu

Phone:608.262.0258

Tehshik Yoon
Yoon, Tehshik P.
Position title:Professor of Chemistry, Associate Chair for the Graduate Program, Director of Graduate Studies

Email:tyoon@chem.wisc.edu

Phone:608.262.2268

Martin Zanni
Zanni, Martin T.
Position title:V. W. Meloche-Bascom Professor of Chemistry

Email:zanni@chem.wisc.edu

Phone:608.262.4783

Affiliate Faculty

Attie, Alan D.
Position title:Jack Gorski Professor of Biochemistry

Email:attie@biochem.wisc.edu

Phone:(608) 262-1372


Engle, Jonathan W.
Position title:Associate Professor

Email:jwengle@wisc.edu

Phone:608 263 5805

Dawei Feng
Feng, Dawei
Position title:Assistant Professor of Materials Science and Engineering and Chemistry

Email:dfeng23@wisc.edu

Phone:608.263.2703

Katrina Forest
Forest, Katrina
Position title:Professor of Bacteriology and Chemistry

Email:forest@bact.wisc.edu

Phone:608.265.3566

Ying Ge
Ge, Ying
Position title:Professor of Cell and Regenerative Biology and Chemistry

Email:ge2@wisc.edu

Phone:608.265.4744

Pupa Gilbert
Gilbert, Pupa
Position title:Professor of Chemistry, Professor of Physics

Email:pupa@physics.wisc.edu

Phone:608.262.5829

Jennifer Golden
Golden, Jennifer
Position title:Associate Professor of Pharmaceutical Sciences and Chemistry

Email:jennifer.golden@wisc.edu

Phone:608.263.7287


Gong, Shaoqin Sarah
Position title:Vilas Distinguished Professor, Advancing Vision Science Chair Professor, and RRF Edwin and Dorothy Gamewell Professor in the Departments of Ophthalmology and Visual Sciences and Chemistry, Wisconsin Institute for Discovery

Email:shaoqingong@wisc.edu

Phone:608.316.4311

Padma Gopalan
Gopalan, Padma
Position title:Professor of Materials Science and Engineering and Chemistry

Email:pgopalan@wisc.edu

Phone:608.265.4258

Aaron Hoskins
Hoskins, Aaron
Position title:Professor of Biochemistry and Chemistry

Email:ahoskins@wisc.edu

Phone:608.890.3101 office, 608.890.4491 lab

Lingjun Li
Li, Lingjun
Position title:Professor of Pharmaceutical Sciences and Chemistry

Email:lli@pharmacy.wisc.edu

Phone:608.265.8491

David Lynn
Lynn, David
Position title:Professor of Chemical and Biological Engineering and Chemistry

Email:dlynn@engr.wisc.edu

Phone:608.262.1086

Sandro Mecozzi
Mecozzi, Sandro
Position title:Professor of Pharmaceutical Sciences and Chemistry

Email:sandro.mecozzi@wisc.edu

Phone:608.262.7810


Neugebauer, Monica
Position title:Assistant Professor

Email:meneugebauer@wisc.edu


Ping, Yuan
Position title:Associate Professor

Email:yping3@wisc.edu


Remucal, Christy
Position title:Associate Professor

Email:remucal@wisc.edu

Phone:(608) 262-1820


Rienstra, Chad
Position title:NMRFAM Co-Investigator, Professor of Biochemistry

Email:crienstra@wisc.edu

Phone:608.261.1167

Marcel Schreier
Schreier, Marcel
Position title:Assistant Professor of Chemical Engineering and Chemistry

Email:mschreier2@wisc.edu

Weiping Tang
Tang, Weiping
Position title:Professor of Pharmaceutical Sciences and Chemistry

Email:wtang@pharmacy.wisc.edu

Phone:608.890.1846


Van Lehn, Reid
Position title:Associate Professor

Email:vanlehn@wisc.edu


Weeks, Amy M.
Position title:Assistant Professor

Email:amweeks@wisc.edu

Phone:608-890-2583


Yesilköy, Filiz
Position title:Assistant Professor

Email:filiz.yesilkoy@wisc.edu

Phone:(608) 262-5112


Yu, Lian
Position title:Professor of Pharmaceutical Sciences and Chemistry

Email:lyu@pharmacy.wisc.edu

Phone:608.263.2263

Emeriti Faculty
Steve Burke
Burke, Steve
Position title:Professor of Chemistry

Email:burke@chem.wisc.edu

Phone:608.262.4941

Charles Casey
Casey, Charles P.
Position title:Homer Adkins Professor Emeritus

Email:casey@chem.wisc.edu

Phone:608.262.0584


Cornwell, Daniel
Flemming Crim
Crim, F. Fleming
Position title:Emeritus Professor of Chemistry

Email:fcrim@chem.wisc.edu

Phone:608.263.7364

Thomas Farrar
Farrar, Thomas C.
Position title:Emeritus Professor of Chemistry

Email:tfarrar@chem.wisc.edu

Phone:608.262.6158

Professor Gaines holds a piece of chemical equipment.
Gaines, Donald
JE Harriman
Harriman, J. E.
Position title:Emeritus Professor of Chemistry

Email:harriman@chem.wisc.edu

Phone:608.262.0264

Laura Kiessling
Kiessling, Laura L.
Position title:Emeritus Professor of Chemistry

Email:kiessling@chem.wisc.edu

Cathy Middlecamp
Middlecamp, Cathy
Position title:Nelson Institute for Environmental Studies Professor and Professor of Chemistry

Email:cathy@chem.wisc.edu

Phone:608.263.5647

John Moore
Moore, John W.
Position title:Emeritus W.T. Lippincott Professor of Chemistry

Email:jwmoore@chem.wisc.edu

Thomas Record
Record, Thomas
Position title:Professor of Chemistry and Biochemistry

Email:record@chem.wisc.edu

Phone:608.262.5332

Bassam Shakhashiri
Shakhashiri, Bassam Z.
Position title:Emeritus Professor of Chemistry

Email:bassam@chem.wisc.edu

Ned Sibert
Sibert, Ned
Position title:Emeritus Professor of Chemistry

Email:sibert@chem.wisc.edu

Phone:608.262.0265

James L Skinner
Skinner, James L.
Position title:Emeritus Professor of Chemistry

Email:skinner@chem.wisc.edu

Professor Taylor
Taylor, James

Treichel, Paul
WE Vaughan
Vaughan, W. E.
Position title:Emeritus Professor of Chemistry

Email:vaughan@chem.wisc.edu

Frank Weinhold
Weinhold, Frank A.
Position title:Emeritus Professor of Chemistry

Email:weinhold@chem.wisc.edu

Phone:608.262.0263

Jim Weisshaar
Weisshaar, James C.
Position title:Richard J. Burke Professor of Chemistry

Email:weisshaar@chem.wisc.edu

Phone:608.262.0266

Claude Woods
Woods, Claude
Position title:Professor of Chemistry

Email:woods@chem.wisc.edu

Phone:608.262.2892

John Wright
Wright, John C.
Position title:Andreas C. Albrecht Professor of Chemistry

Email:wright@chem.wisc.edu

Phone:608.262.0351


Yu, Hyuk
Position title:Emeritus Professor of Chemistry

Email:hyukyu@mhtc.net

Phone:608-574-4381

Site footer content
Part of the Universities of Wisconsin
Quick Links
Directory
Graduate Degree Programs
Undergraduate
Employment at Chemistry
Safety
Contact Us
Normal
Undergraduate Office
Graduate Office
Communications
Webmaster
Contact Us
1101 University Avenue
Madison, WI 53706
Map
Email: connect@chem.wisc.edu
Phone: (608) 262-1486
Website feedback, questions or accessibility issues: connect@chem.wisc.edu | Learn more about accessibility at UW–Madison.

This site was built using the UW Theme | Privacy Notice | © 2024 Board of Regents of the University of Wisconsin System.

Cookie Notice
We use cookies on this site. By continuing to browse without changing your browser settings to block or delete cookies, you agree to the UW–Madison Cookie Notice.
Accept cookie notice
Skip to main content
University of Wisconsin–Madison
Department of Communication Arts
University of Wisconsin-Madison
Search
Search
Home
Undergraduate
Graduate
Courses
People
Alumni
Giving
About
Instructional Media Center
Log-In
Home
People
People
Faculty
Robert
Robert Asen
Rhetoric, Politics, and Culture

Professor

robert.asen@wisc.edu

608-263-1418

6142 Vilas Hall

Anirban Baishya
Anirban Baishya
Rhetoric, Politics, & Culture

Assistant Professor

abaishya@wisc.edu

6014 Vilas Hall

Kelley Conway
Kelley Conway
Film

Professor

kelleyconway@wisc.edu

608-263-3921

6170 Vilas Hall

Craig Erpelding
Craig Erpelding
Film

Teaching Faculty

cerpelding@wisc.edu

6072 Vilas Hall

Professor Jonathan Gray
Jonathan Gray
Media and Cultural Studies

Professor

jagray3@wisc.edu

608-263-2541

6146 Vilas Hall

Aaron Greer
Aaron Greer
Film

Associate Professor

adgreer@wisc.edu

608-262-7971

6052 Vilas Hall

Erik Gunneson
Erik Gunneson
Film

Teaching Faculty

gunneson@wisc.edu

608-263-4091

6033 Vilas Hall

Professor Robert Howard
Robert Glenn Howard
Rhetoric, Politics, and Culture

Professor

rghoward2@wisc.edu

608-262-2605

6040 Vilas Hall

Eric Hoyt
Eric Hoyt
Media and Cultural Studies; Film

Professor

ehoyt@wisc.edu

608-262-1637

6038 Vilas Hall

Sarah Jedd
Sarah Jedd
Rhetoric, Politics, and Culture

Teaching Faculty

sjedd@wisc.edu

608-347-9627

6172 Vilas Hall

Derek Johnson
Derek Johnson
Media and Cultural Studies

Department Chair, Professor

drjohnson3@wisc.edu

608-262-8788

6110 Vilas Hall


Jenell Johnson
Rhetoric, Politics, and Culture

Professor

jenell.johnson@wisc.edu

608-262-4921

6037 Vilas Hall

Professor Jason Lopez
Jason Kido Lopez
Media and Cultural Studies

Assistant Professor

jason.lopez@wisc.edu

608-262-1872

6136 Vilas Hall

Professor Lori Kido-Lopez
Lori Lopez
Media and Cultural Studies

Professor of Communication Arts

lklopez@wisc.edu

Email only

6134 Vilas Hall

Professor Marie-Louise Mares
Marie-Louise Mares
Communication Science

Professor

mares@wisc.edu

608-263-2350

6140 Vilas Hall


Mary McCoy
Rhetoric, Politics, and Culture

Teaching Faculty

mccoy2@wisc.edu

608-263-1755

0207 Ingraham Hall

Professor Sara McKinnon
Sara McKinnon
Rhetoric, Politics, and Culture

Professor

smckinnon@wisc.edu

608-262-2417 (office phone)

6035 Vilas Hall


Darshana Sreedhar Mini
Film

Assistant Professor

dmini@wisc.edu

608-262-2527

6016 Vilas Hall

Jeremy Morris
Jeremy Morris
Media and Cultural Studies

Professor | Director of Graduate Studies

jwmorris2@wisc.edu

608-262-1135

6132 Vilas Hall

Professor Zhongdong Pan
Zhongdang Pan
Communication Science

Professor

zhongdangpan@wisc.edu

608-263-3920

6138 Vilas Hall

Allison
Allison Prasch
Rhetoric, Politics, and Culture

Associate Professor

aprasch@wisc.edu

Professor Ben Singer
Ben Singer
Film

Associate Professor

ben.singer@wisc.edu

608-263-3923

6054 Vilas Hall

Professor Jeff Smith
Jeff Smith
Film

Professor

jpsmith8@wisc.edu

608-263-3132

6150 Vilas Hall


Juhyung Sun
Communication Science

Visiting Assistant Professor

juhyung.sun@wisc.edu

6167 Vilas Hall

Professor Catalina Toma
Catalina Toma
Communication Science

Professor

ctoma@wisc.edu

608-262-8760

6144 Vilas Hall


Lyn van Swol
Communication Science

Professor

vanswol@wisc.edu

608-262-1947

6152 Vilas Hall


Lillie Williamson
Communication Science

Assistant Professor

ldwilliamso2@wisc.edu

608-263-3965

6156 Vilas Hall

Associate Dean for Advancement, Arts & Humanities Sue Zaeske
Susan Zaeske
Rhetoric, Politics, and Culture

Professor

szaeske@wisc.edu

608-263-7221

Staff
Lindsey Cardell
Lindsey Cardell

Communications Specialist

ljcardell@wisc.edu

3159 Vilas Hall

Daniel Feurer
Daniel Feuer

Graduate Coordinator

daniel.feuer@wisc.edu

608-262-3398

6056 Vilas Hall

Phil Gandolph
Phil Gandolph

Shipping & Mailing Associate

phil.gandolph@vilas.uwex.edu

608-262-6245

2096 Vilas Hall

Steffie Halverson
Steffie Halverson

Undergraduate Advisor

halverson2@wisc.edu

608-262-2285

6114 Vilas Hall

Jim Healy
Jim Healy

Director of Cinematheque Film Programming

jehealy@wisc.edu

608-263-9643

6031 Vilas Hall

Boyd Hillestad
Boyd Hillestad

Media Technician

bjhilles@wisc.edu

608-263-4496

3030 Vilas Hall

Sophie Hougland
Sophie Hougland

Office Assistant

shougland@wisc.edu

608-262-2277

6110 Vilas Hall


Mary Huelsbeck

Assistant Director, Wisconsin Center for Film and Theater Research

huelsbeck@wisc.edu

608-262-9706

6039 Vilas Hall

Terry Kerr
Terry Kerr

Outreach Coordinator

terry.kerr@wisc.edu

Michael King
Michael King

Academic Curator

msking3@wisc.edu

608-262-3627

4022 Vilas Hall


Lynn Malone

Department Administrator

lynn.malone@wisc.edu

608-262-2544

6112 Vilas Hall

Ben Reiser
Ben Reiser

Outreach Program Manager

ben.reiser@wisc.edu

608-262-3627

4022 Vilas Hall

Kathleen Ricci
Kathleen Ricci

Development Specialist

kricci@wisc.edu

Mary Rossa
Mary Rossa

Undergraduate Advisor

mary.rossa@wisc.edu

608-262-0992

6068 Vilas Hall


Ken Sabbar

Computer Specialist

sabbar@wisc.edu

608-263-4090

3158 Vilas Hall

Clara Schanck
Clara Schanck

Undergraduate Assistant

cschanck@wisc.edu

608-263-0747

6117 Vilas Hall

Amy Schultz
Amy Schultz

Digital Certificate Advisor

amy.schultz@wisc.edu

608-262-2547

6050 Vilas Hall

Pete Segnock
Peter Sengstock

Director of Media Services

pgsengstock@wisc.edu

608-263-2296

3157 Vilas Hall

Katrina Simyab
Katrina Simyab

Communication Specialist WFFC

simyab@wisc.edu


Amanda Smith
Wisconsin Center for Film and Theater Research

Film Archivist

amsmith56@wisc.edu

608-264-6467

435 State Historical Society
816 State Street
Madison, WI 53706

Julie Van Esler
Julie Van Esler

IMC Manager

jvanesler@wisc.edu

608-265-4231

3159 Vilas Hall

Graduate Students
Yusuf Akinyemi
Yusuf Akinyemi
Rhetoric, Politics, and Culture

Teaching Assistant

yakinyemi@wisc.edu

608-263-3997

6067 Vilas Hall

Gaurav Aung
Gaurav Aung
Rhetoric, Politics, and Culture

Teaching Assistant

wnaung@wisc.edu

608-263-9644

6053 Vilas Hall

Madison Barnes-Nelson
Madison Barnes-Nelson
Media and Cultural Studies

Teaching Assistant

barnesnelson@wisc.edu

608-265-2222

2157 Vilas Hall


Kallan Benjamin
Film

Fellow

knbenjamin@wisc.edu

608-263-3133

2155 Vilas Hall

John Bennett
John Bennett
Film

Teaching Assistant

jpbennett@wisc.edu

608-263-3133

2155 Vilas Hall

Eric Boateng
Eric Boateng
Rhetoric, Politics, and Culture

Teaching Assistant

eboateng2@wisc.edu

608-263-0490

6164 Vilas Hall

Tom Brami
Tom Brami
Film

Dissertator

tmacpherson@wisc.edu

Off-Campus

Timothy Brayton
Timothy Brayton
Film

Teaching Assistant

tbrayton@wisc.edu

608-265-6926

2156 Vilas Hall


Laura Broman
Media and Cultural Studies

Fellow

lbroman@wisc.edu

608-263-2039

2153 Vilas Hall

Minh Bui
Minh Bui
Film

Teaching Assistant

mabui@wisc.edu

608-263-3999

2147 Vilas Hall

Tammy Chang
Chen-Ting Chang
Communication Science

Dissertator

cchang226@wisc.edu

Off-Campus


Jinyoung Choi
Communication Science

Teaching Assistant

jinyoung.choi@wisc.edu

608-263-3996

6051 Vilas Hall

Brook Couch
Brook Couch
Communication Science

Teaching Assistant

blcouch@wisc.edu

608-263-3998

6166 Vilas Hall

Ika Dai
Ika Dai
Communication Science

Teaching Assistant

ydai53@wisc.edu

608-263-9644

6053 Vilas Hall

Ephraim Danquah
Ephraim Danquah
Rhetoric, Politics, and Culture

Teaching Assistant

esdanquah@wisc.edu

608-263-3997

6067 Vilas Hall

Shuvam Das
Shuvam Das
Media and Cultural Studies

Teaching Assistant

sdas65@wisc.edu

608-263-3999

2147 Vilas Hall

Ben
Ben Davis
Media and Cultural Studies

Teaching Assistant

btdavis3@wisc.edu

608-265-6928

2152 Vilas Hall

Pate Duncan
Pate Duncan
Film

Teaching Assistant

pwduncan@wisc.edu

608-263-2039

2153 Vilas Hall


Sarah Edwards
Media and Cultural Studies

Teaching Assistant

seedwards2@wisc.edu

608-265-4856

2151 Vilas Hall

Finke Klachko
Sabrina Finke-Klachko
Communication Science

Teaching Assistant

sfinke@wisc.edu

608-263-3998

6166 Vilas Hall

Lore FitzWhittemore
Lore FitzWhittemore
Media and Cultural Studies

Teaching Assistant

twhittemore@wisc.edu

608-263-3999

2147 Vilas Hall

Sarah Mae Fleming
Sarah Mae Fleming
Film

Teaching Assistant

sdfleming@wisc.edu

2156 Vilas Hall

Allyson Gross
Allyson Gross
Rhetoric, Politics, and Culture

Fellow

aagross2@wisc.edu

608-263-0490

6164 Vilas Hall

Hsuan-I Huang
Hsuan-I Huang
Rhetoric, Politics, and Culture

Teaching Assistant

hsuani.huang@wisc.edu

608-263-9644

6053 Vilas Hall

Rachel Hutchins
Rachel Hutchins
Communication Science

Fellow

rhutchins2@wisc.edu

608-263-3998

6166 Vilas Hall

Mattie Jacobs
Mattie Jacobs
Film

Project Assistant

mcjacobs4@wisc.edu

2154 Vilas Hall

Samantha Janes
Samantha Janes
Film

Teaching Assistant

sjanes2@wisc.edu

608-265-6928

2152 Vilas Hall

Max Kaplan
Max Kaplan
Media and Cultural Studies

Teaching Assistant

mwkaplan@wisc.edu

608-265-6909

2158 Vilas Hall


Pauline Lampert
Film

Teaching Assistant

plampert@wisc.edu

608-263-3133

2155 Vilas Hall

Ashton Leach
Ashton Leach
Film

Project Assistant

aaleach@wisc.edu

608-265-6926

2156 Vilas Hall

Zexuan Lin
Zexuan Lin
Communication Science

Teaching Assistant

zlin254@wisc.edu

608-263-3996

6051 Vilas Hall

litt
Aranveer Litt
Rhetoric, Politics, and Culture

Teaching Assistant

aslitt@wisc.edu

608-263-9644

6053 Vilas Hall

Mary Lu
Mary Lu
Communication Science

Teaching Assistant

rlu34@wisc.edu

608-263-3996

6051 Vilas Hall

Zhi Luo
Zhi Luo
Rhetoric, Politics, and Culture

Teaching Assistant

zluo226@wisc.edu

608-263-3997

6067 Vilas Hall

Josh Martin
Josh Martin
Film

Teaching Assistant

jrmartin8@wisc.edu

608-265-6927

2154 Vilas Hall

David Martinez
David Martinez
Film

Fellow

david.martinez@wisc.edu

608-263-3999

2147 Vilas Hall


Matthew Meier
Communication Science

Teaching Assistant

mlmeier2@wisc.edu

608-263-3998

6166 Vilas Hall

At The Heart Of Gold
Ailea Merriam-Pigg
Rhetoric, Politics, and Culture

Lecturer

merriampigg@wisc.edu

608-263-0490

6164 Vilas Hall

Mo Shiwei
Shiwei Mo
Communication Science

Teaching Assistant

smo5@wisc.edu

608-263-3996

6051 Vilas Hall

Ceci Moffett
Ceci Moffett
Media and Cultural Studies

Teaching Assistant

clmoffett@wisc.edu

608-265-6909

2158 Vilas Hall

Julian Mueller-Herbst
Julian Mueller-Herbst
Communication Science

Dissertator

muellerherbs@wisc.edu

Off-Campus

Marianne
Marianne Nacanaynay
Media and Cultural Studies

Teaching Assistant

nacanaynay@wisc.edu

608-265-7525

2150 Vilas Hall


Clare O'Gara
Media and Cultural Studies

Teaching Assistant

cogara@wisc.edu

2151 Vilas Hall

Nicole Pacelli
Nicole Pacelli
Film

Teaching Assistant

npacelli@wisc.edu

608-263-3133

2147 Vilas Hall

Jiwon Park
Jiwon Park
Media and Cultural Studies

Teaching Assistant

jiwon.park@wisc.edu

608-263-3999

2147 Vilas Hall

Miranda Perry
Miranda Perry
Rhetoric, Politics, and Culture

Teaching Assistant

mnperry@wisc.edu

608-263-9644

6053 Vilas Hall

Ben Pettis
Ben Pettis
Media and Cultural Studies

Teaching Assistant, Project Assistant

bpettis@wisc.edu

608-265-4856

2151 Vilas Hall


Kai Prins
Rhetoric, Politics, and Culture

Project Assistant

kprins@wisc.edu

608-263-0490

6164 Vilas Hall

Areyana Proctor
Areyana Proctor
Media and Cultural Studies

Teaching Assistant

ajproctor@wisc.edu

2150 Vilas Hall

Will Quade
Will Quade
Film

Fellow

wquade@wisc.edu

608-265-6928

2152 Vilas Hall

Sara Rabon
Sara Rabon
Rhetoric, Politics, and Culture

Teaching Assistant

srabon@wisc.edu

608-263-0490

6164 Vilas Hall

Cassidy Rempel
Cassidy Rempel
Rhetoric, Politics, and Culture

Teaching Assistant

crempel@wisc.edu

608-263-3997

6067 Vilas Hall

Olivia Riley
Olivia Riley
Media and Cultural Studies

Teaching Assistant

ojriley@wisc.edu

608-265-2222

2157 Vilas Hall

Alicen Rushevics
Alicen Rushevics
Rhetoric, Politics, & Culture

Teaching Assistant

rushevics@wisc.edu

608-263-9644

6053 Vilas Hall

Dominique Salas
Dominique Salas
Rhetoric, Politics, and Culture

Dissertator

dsalas2@wisc.edu

Off-Campus

Nick Sansone
Nick Sansone
Film

Teaching Assistant

nsansone@wisc.edu

608-265-7525

2150 Vilas Hall

Nimish Sarin
Nimish Sarin
Film

Teaching Assistant

nsarin@wisc.edu

608-263-3999

2147 Vilas Hall

Cheryl Shea
Cheryl Shea
Communication Science

Teaching Assistant

cheryl.shea@wisc.edu

608-263-3996

6051 Vilas Hall

Liwei Shen
Liwei Shen
Communication Science

Dissertator

lshen36@wisc.edu

608-263-3996

6051 Vilas Hall

Bengisu Simsek
Bengisu Şimşek
Communication Science

Teaching Assistant

bsimsek@wisc.edu

608-263-3998

6166 Vilas Hall


Shreya Singh
Rhetoric, Politics, and Culture

Lecturer

shreya.singh@wisc.edu

608-263-3997

6067 Vilas Hall

Matt St. John
Matt St. John
Film

Project Assistant

mdstjohn@wisc.edu

6018 Vilas Hall


Lance St. Laurent
Film

Project Assistant

stlaurent@wisc.edu

608-265-6927

2154 Vilas Hall

Lesley Stevenson
Lesley Stevenson
Media and Cultural Studies

Fellow

lcstevenson@wisc.edu

608-265-6909

2158 Vilas Hall

Garrett Stpko
Garrett Strpko
Film

Teaching Assistant

strpko@wisc.edu

608-263-3999

2147 Vilas Hall


Shannon Weidner
Film

Teaching Assistant

scweidner@wisc.edu

608-263-2039

2153 Vilas Hall

Tom Welch
Thomas Welch
Media and Cultural Studies

Teaching Assistant

thomas.welch@wisc.edu

608-265-7525

2150 Vilas Hall
Office Hours: Wednesdays, 1–3 PM

Anya Williams
Anya Williams
Film

Teaching Assistant

akwilliams7@wisc.edu

608-263-2039

2153 Vilas Hall

Taylore Woodhouse
Taylore Woodhouse
Media and Cultural Studies

Lecturer

tnwoodhouse@wisc.edu

608-265-2222

2157 Vilas Hall


Nathan Workman
Media and Cultural Studies

Lecturer

nworkman@wisc.edu

608-265-2222

2158 Vilas Hall


Ryna Yeoh
Communication Science

Teaching Assistant

ryeoh@wisc.edu

608-263-3998

6166 Vilas Hall

Xiaotong Zhang
Xiaotong Zhang
Communication Science

Teaching Assistant

xiaotong.zhang@wisc.edu

608-263-3998

6166 Vilas Hall

Han Zhou
Han Zhou
Communication Science

Teaching Assistant

hzhou365@wisc.edu

608-263-3996

6051 Vilas Hall

Rhea Zhu
Rhea Zhu
Communication Science

Fellow

rzhu228@wisc.edu

608-263-9644

6067 Vilas Hall

Additional Teaching Assistants
Jude Balthazar
Jude Balthazar

Teaching Assistant

balthazar2@wisc.edu

608-263-3998

6166 Vilas Hall

Maggie Cremers
Maggie Cremers

Teaching Assistant

mcremers@wisc.edu

608-263-3997

6067 Vilas Hall

Payton Cushman
Payton Cushman

Teaching Assistant

pcushman@wisc.edu

608-263-0490

6164 Vilas Hall

Rudy Dieudonne
Rudy Dieudonne

Teaching Assistant

dieudonne@wisc.edu

608-263-3999

2147 Vilas Hall

Sneha Dutta Roy
Sneha Dutta Roy

Teaching Assistant

sduttaroy@wisc.edu

608-263-5488

2078 Vilas Hall

Grady Hayden
Grady Hayden

Teaching Assistant

ghayden2@wisc.edu

608-263-5488

2078 Vilas Hall

Zach Holden
Zach Holden

Teaching Assistant

zholden2@wisc.edu

608-263-5488

2078 Vilas Hall

Anastasiia Johnson
Anastasiia Johnson

Teaching Assistant

ishmuratova@wisc.edu

608-263-3133

2155 Vilas Hall

Alden Laev
Alden Laev

Teaching Assistant

laev@wisc.edu

608-263-3996

6051 Vilas Hall

Francesco Liucci
Francesco Liucci

Teaching Assistant

liucci@wisc.edu

608-263-0490

6164 Vilas Hall

Gary Lu
Gary Lu

Teaching Assistant

gary.lu@wisc.edu

608-263-5488

2078 Vilas Hall

Zoe Miller
Zoe Miller

Teaching Assistant

zemiller3@wisc.edu

608-263-9644

6053 Vilas hall

Adam Nissenbaum
Adam Nissenbaum

Teaching Assistant

anissenbaum@wisc.edu

608-263-3997

6067 Vilas Hall

Avalon Ruby
Avalon Ruby

Teaching Assistant

aaruby@wisc.edu

608-263-3999

2147 Vilas Hall

Kelby Schnepel
Kelby Schnepel

Teaching Assistant

schnepel@wisc.edu

608-263-5488

2078 Vilas Hall

Lily Shell
Lily Shell

Teaching Assistant

lshell@wisc.edu

608-263-2039

2153 Vilas Hall

Jacob Sorrells
Jacob Sorrells

Teaching Assistant

jsorrells@wisc.edu

608-263-0490

6164 Vilas Hall

Opeoluwa Taiwo
Opeoluwa Taiwo

Teaching Assistant

ostaiwo@wisc.edu

608-263-5488

2078 Vilas Hall

Yanshu Sybil Wang
Yanshu Sybil Wang

Teaching Assistant

ywang3424@wisc.edu

608-263-5488

2078 Vilas Hall

Claire Whitney
Claire Whitney

Teaching Assistant

crwhitney2@wisc.edu

608-263-3996

6051 Vilas Hall

Emeriti
Tino Balio
Tino Balio
Film

Professor Emeritus

tbalio@wisc.edu

David Bordwell
David Bordwell
Film

Professor Emeritus

bordwell@wisc.edu

Joanne Cantor
Joanne Cantor
Communication Science

Professor Emerita

jrcantor@wisc.edu

Michele Hilmes
Michele Hilmes
Media and Cultural Studies

Professor Emerita

mhilmes@wisc.edu

Professor Lea Jacobs
Lea Jacobs
Film

Professor Emerita

lea.jacobs@wisc.edu

Nietzchka Keene
Nietzchka Keene
Film

Professor Emerita


Professor Emeritus Vance Kepley
Vance Kepley
Film

Professor Emeritus

vikepley@wisc.edu

Professor Steve Lucas
Stephen Lucas
Rhetoric, Politics, and Culture

Professor Emeritus

selucas@wisc.edu

Professor J.J. Murphy
J.J. Murphy
Film

Professor Emeritus

jjmurphy@wisc.edu

Site footer content
Quick Links
Instructional Media Center
Undergraduate Advising
CommArts KB
CommArts Internal KB
Contact Us
6116 Vilas Hall
821 University Ave
Madison, WI 53706
Email: info@commarts.wisc.edu
Website feedback, questions or accessibility issues: info@commarts.wisc.edu.

Learn more about accessibility at UW–Madison.

This site was built using the UW Theme | Privacy Notice | © 2024 Board of Regents of the University of Wisconsin System.


"""

email_addresses = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)

for email in email_addresses:
    print(email)