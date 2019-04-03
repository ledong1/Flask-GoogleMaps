from flask import Flask, render_template
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map

app = Flask(__name__)
GoogleMaps(app, key="AIzaSyA1bLqqQwj8Ls4E_fcK-YTpc_pL_oJZ3ko")

@app.route("/")
def mapview():
    # creating a map in the view
    sndmap = Map(
        identifier="sndmap",
        lat=38,
        lng=104.2115,
        zoom=4.3,
        markers=[
          {
             'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
             'lat': 25.3623,
             'lng': 100.1603,
             'infobox': "<h1>白族</h1><br><img src='http://5b0988e595225.cdn.sohucs.com/images/20170907/9a26742c35624761b5bc7b98d7f8509e.jpeg' />"
          },
          {
             'icon': 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png',
             'lat': 31.58,
             'lng': 87.04,
             'infobox': "<h1>藏族</h1><img src='http://5b0988e595225.cdn.sohucs.com/images/20170907/b6216cfae08a44ae9168065db63f2f46.jpeg' />"
          },
          {
             'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
             'lat': 24.77,
             'lng': 103.77,
             'infobox': "<h1>彝族</h1><br><img src='http://5b0988e595225.cdn.sohucs.com/images/20170907/55038fa9ef2e45e981d34e927ffc3c7f.jpeg' />"
          },
          {
             'icon': 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png',
             'lat': 45.39,
             'lng': 122.9394,
             'infobox': "<h1>朝鲜族</h1><br><img src='http://5b0988e595225.cdn.sohucs.com/images/20170907/3e0a3f38849248bcbb3fbdddb0397501.jpeg' />"
          },
          {
             'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
             'lat': 40.50,
             'lng': 85.61,
             'infobox': "<h1>维吾尔族</h1><br><img src='http://5b0988e595225.cdn.sohucs.com/images/20170907/e10482654a2144a5b0ba348d0770600e.jpeg' />"
          },
          {
             'icon': 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png',
             'lat': 23.80,
             'lng': 99.35,
             'infobox': "<h1>哈尼族</h1><br><img src='http://5b0988e595225.cdn.sohucs.com/images/20170907/e0310d9f27af4523a752f27ce3f086b6.jpeg' />"
          },
        ],
        style="height:720px;width:1500px;margin:0;",
        region="CN"
    )
    return render_template('a.html',  sndmap=sndmap)

if __name__ == "__main__":
    app.run(debug=True)
