import base64
import getpass
import urllib.parse

password = getpass.getpass()
urlEncodedPassword = urllib.parse.quote(password)
p = base64.b64encode(urlEncodedPassword.encode()).decode()
print(p)
