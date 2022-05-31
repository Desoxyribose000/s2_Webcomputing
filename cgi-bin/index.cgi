#!/usr/bin/python
import cgi

form=cgi.FieldStorage()

liter=float(form['liter'].value)
tropfen=float(form['tropfen'].value)
klinken=float(form['tuerklinken'].value)

tage=int(liter/(tropfen*0.005*klinken))


print("Content-Type: text/html")
print("")
print("<!DOCTYPE html>")
print('<html lang="DE">')
print('''
<head>
<meta charset="UTF-8">
<link href="./../style/style.css" type="text/css" 
rel="stylesheet">
<title>Covid-19-Infoseite</title>
</head>


<body>
<div id="wrapper">

    <div class="navbar">
        <nav class="navtop">
            <div class="content nav">
                <div id="logo">    
                    <img src="./../media/logo.jpg" 
width="50" alt="DNA-Logo">
                </div>
                <nav class="nav-menu">

                    <a class="navlink top-navlink current" 
href="./../index.html">Home</a>
                    <a class="navlink top-navlink" 
href="./../index.html">Home</a>
                    <a class="navlink top-navlink" 
href="./../index.html">Home</a>
                    <a class="navlink top-navlink" 
href="./../index.html">Home</a>
                    <a class="navlink top-navlink" 
href="./../index.html">Home</a>

                </nav>
             </div>
         </nav>
    </div>
    
    <div class="navbottom">
        <div class="content flex">
            <a href="#main" id="headline">
                <h5 class="nav-header">
                    <span class="blue">Top</span>
                </h5>
            </a>
            <div class="sub-nav">

                <a class="navlink bottom-navlink" 
href="#symptome">Symptome</a>
                <a class="navlink bottom-navlink" 
href="#ziel">Ziel</a>
                <a class="navlink bottom-navlink" 
href="#schutz">Schutz</a>
                <a class="navlink bottom-navlink" 
href="#rechner">Ergebnis</a>
             </div>
        </div>
    </div>

    <div id="main">
        <div id="top" class="section">
            <br>
            <div class="restricted">
                <h2>Was ist Covid-19?</h2>
                <p class="subtext">
                Der Coronavirus (Covid-19), der die Welt seit den letzten Monaten des Jahres 2019 bewegt, ist f&uuml;r viele Menschen immer noch ein Mysterium.<br>Woher stammt das Virus? Dieses hat seinen Anfang in der Stadt Wuhan gegen Dezember des Jahres 2019 gefunden. Die naheliegendste Vermutung geht davon aus, dass das Virus seinen Ursprung am jetzt weltbekannten Huanan Fischmarkt hat.<br>Dort soll das Virus urspr&uuml;nglich von Flederm&auml;usen auf den Menschen oder zuerst auf das G&uuml;rteltier, als &Uuml;bertragungsglied, und dann auf den Menschen &uuml;bertragen worden sein. 
                </p>
            </div>
            
            <div id="person_p" class="parallex"></div>
            </div>
            <div id="symptome" class="section">
	       <div class="restricted">
		<h5>Symptome</h5>
                <p class="subtext">
                Das Coronavirus wird durch Tr&ouml;pfcheninfektion verbreitet. Dabei sind die h&auml;ufigsten Symptome Fieber, trockener Husten und M&uuml;digkeit. Seltener sind Symptome wie Schmerzen, eine verstopfte Nase, Kopfschmerzen, Bindehautentz&uuml;ndung, ein trockener Hals, Durchfall, Verlust des Geschmacks- und oder Geruchssinns, Hautausschlag und Verf&auml;rbung von Fingern und Zehen auf. F&uuml;r den Fall das Symptome auftreten, sollte man sich selbst isolieren und zu Hause bleiben, sowie Personen, mit denen man in Kontakt gekommen ist, informieren.
                </p>
           </div>

           <div id="VIRUS_p" class="parallex"></div>
        </div>

        <div id="ziel" class="section flex center">
	   <div class="content">
		<div class="_50 left">
		    <h5>Ziel</h5>
		</div>
	   </div>

            <div class="content subtext">
                
                <div class="_50 left">
                Das wichtigste Ziel im Moment ist die Infektionsrate so weit wie m&ouml;glich zu reduzieren. Wenn wir dies erreichen, k&ouml;nnen wir durch eine reduzierte Belastung von Krankenh&auml;usern mehr Patienten bestm&ouml;glich versorgen. Auch wenn nur ca. 20 Prozent aller Infizierten eine ernsthafte Behandlung im Krankenhaus brauchen, kann eine hohe Infektionsrate zu einer starken Auslastung der Krankenh&auml;user und weniger Behandlungsressourcen f&uuml;hren.<br> Ein weiterer wichtiger Punkt ist die Lockerung von Ma&szlig;nahmen zur Eind&auml;mmung des Virus. Zwar ist die Aussicht, nach einer erfolgreichen Eind&auml;mmung, zum normalen Leben zur&uuml;ckzukehren vielversprechend, aber auch risikobelastet. So k&ouml;nnte es zu einer noch viel gravierenden zweiten Infektionswelle kommen.
                </div>

            </div>
            <div class="fullboxhalf right">
                <div id="doctors_i" class="fullimage"></div>
            </div>
        </div>
        <div id="schutz" class="section">
	   <div class="restricted">
		<h5>Schutz</h5>
	   </div>
	    <div class="textcont">
            <div class="textpanel">
                <h5>Masken als Schutz</h5>
                <p class="subtext">
                Zwar wurde f&uuml;r viele Bereiche des Lebens schon die Maskenpflicht eingef&uuml;hrt, aber dennoch sollte man in den Bereichen, wo diese noch nicht besteht, Eigenverantwortung &uuml;bernehmen. Auch kann man Masken selbst n&auml;hen und Leuten, die keine haben, welche zukommen lassen.
                </p>
            </div>
            <div class="textpanel dark">
            <h5>Abstand halten</h5>
            <p class="subtext">
            Bei der schon genannten &Uuml;bertragungsart der Tr&ouml;pfcheninfektion, sollte das Anfassen von Augen, Nase und Mund vermieden werden. Das Tragen einer Maske hilft auch beim Vermeiden von impulsiven Ber&uuml;hrungen des Gesichts.<br>Auch das Einhalten des Mindestabstands von 1,5 Metern und das Vermeiden sozialer Kontakte hilft bei der Infektionsvorbeugung.
            </p>
            </div>
            
            <div class="textpanel">
            <h5>Homeoffice und Desinefektionsmittel</h5>
            <p class="subtext">
            Au&szlig;erdem sollte man seine H&auml;nde regelm&auml;&szlig;ig waschen und oder desinfizieren und anderen die M&ouml;glichkeit der Desinfektion bereitstellen.<br>Zwei letzte Punkte w&auml;ren das Arbeiten von Zuhause und das Bewahren von Ruhe. Vor allen Dingen das Arbeiten von zu Hause oder auch das Arbeiten in Schichten mit weniger Betrieb sind Wege sich selbst und andere weniger zu gef&auml;hrden. Beim Bewahren von Ruhe geht es darum sich nicht unn&ouml;tig unter Stress zu setzen, da man an der Situation wenig &auml;ndern und diese nur auswarten kann.
            </p>
            </div>
        </div>
	</div>
        <div id="rechner" class="section">
	<div class="restricted">
                <div class="textpanel">
                    <p class="subtext">
                    ''')
if tage==1:
    print('''
    Ihr Desinfektionsmittel reicht bei aktiver Benutzung nur noch 
    f&uuml;r einen Tag aus. Sie sollten so schnell wie m&ouml;glich 
    neues kaufen. Und denken sie daran eine Maske in L&auml;den 
    aufzusetzen und den Mindestabstand einzuhalten!
    ''')
elif tage==0:
    print('''
    Ihr Desinfektionsmittel reicht bei aktiver Benutzung f&uuml;r 
    keinen ganzen Tag mehr aus. Sie sollten so schnell wie m&ouml;glich 
    neues kaufen.
    Und denken sie daran eine Maske in L&auml;den aufzusetzen und den 
    Mindestabstand einzuhalten!
     ''')
elif tage<7:
    print('''
    Ihr Desinfektionsmittel reich bei aktiver Benutzung f&uuml;r {t} 
    Tage aus. Sie sollten vorausplanen neues zu kaufen.
    '''.format(t=tage))
else:
    print('''
    Ihr Desinfektionsmittel reich bei aktiver Benutzung f&uuml;r {t} 
    Tage aus.
    '''.format(t=tage))
print('''
                    </p>
                </div></div>
            </div>
        </div>
        <div id="footer">      
            <a class="link" href="https://www.th-brandenburg.de/startseite/">
            <img class="w-back" src="https://upload.wikimedia.org/wikipedia/commons/f/f7/Technische_Hochschule_Brandenburg_Logo.svg" 
            height="50" alt="Logo der Technischen Hochschule Brandenburg">
            </a>
        </div>
     </div>

</body>
</html>
''')
