import cgi
from http import cookies
import os

form = cgi.FieldStorage()

text1 = form.getfirst("text-1", "не задано")
text2 = form.getfirst("text-2", "не задано")
if form.getvalue("tern") :
    tern = form.getvalue("tern")
else : tern = ""
if form.getvalue("if") :
    ivano = form.getvalue("if")
else : ivano = ""
if form.getvalue("cher") :
    cher = form.getvalue("cher")
else : cher = ""
if form.getvalue("lviv") :
    lviv = form.getvalue("lviv")
else : lviv = ""
if form.getvalue("food"):
    food = form.getvalue("food")
else : food = "немає"

cs = cookies.SimpleCookie(os.environ["HTTP_COOKIE"])
counter = cs.get("counter")

if counter is None:
    print("Set-cookie: counter=0")
else:
    counterVal = int(counter.value)
    counterVal += 1
    print("Set-cookie: counter={}".format(counterVal))



print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
           <meta charset="UTF-8">
			<meta http-equiv="X-UA-Compatible" content="IE=edge">
			<meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Обробка даних форм</title>
        </head>
        <body>""")

print("<h1>Обробка даних форм!</h1>")
print("<p>Перший текст: {}</p>".format(text1))
print("<p>Другий текст: {}</p>".format(text2))
print("<p>Улюблені міста: {} {} {} {}</p>".format(tern,ivano,cher,lviv))
print("<p>Улюблена їжа: {}</p>".format(food))
print("""</body>
        </html>""")