# Example: https://help.pythonanywhere.com/pages/RedirectWebApp

from flask import Flask, redirect, request
from urllib.parse import urlparse, urlunparse

app = Flask(__name__)

# Target Domain
targetURL = "githib.org"
# URL for Redirection
redirectURL = "github.com/hibbertda"

@app.before_request
def redirectToURL():
    urlparts = urlparse(request.url)
    if urlparts.netloc == targetURL:
        urlparts_list = list(urlparts)
        urlparts_list[1] = redirectURL
        return redirect(urlunparse(urlparts_list), code=301)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)        