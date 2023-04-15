"""
                <ol class="carousel-indicators">
                  <li data-target="#galleycarousel" data-slide-to="0" class="active"></li>
                  <li data-target="#galleycarousel" data-slide-to="1"></li>
                  <li data-target="#galleycarousel" data-slide-to="2"></li>
                </ol>
                <div class="carousel-inner">
                  <div class="carousel-item active">
                    <img src="/imgs/gallery/Kép11.jpg" class="d-block w-100" alt="...">
                  </div>
                  <div class="carousel-item">
                    <img src="/imgs/gallery/Kép13.jpg" class="d-block w-100" alt="...">
                  </div>
                  <div class="carousel-item">
                    <img src="/imgs/gallery/Kép12.jpg" class="d-block w-100" alt="...">
                  </div>
                </div>
"""
import os
rootdir = './'
i = 0
first_html = "<ol class='carousel-indicators'><li data-target='#galleycarousel' data-slide-to='0' class='active'></li>'"
sec_html = "<div class='carousel-inner'>"
for file in os.listdir(rootdir):
    if(file.split(".")[1] == "jpg" or file.split(".")[1] == "png" or file.split(".")[1] == "jpeg"):
        first_html += "<li data-target='#galleycarousel' data-slide-to='"+str(i)+"'></li>"

        sec_html += "<div class='carousel-item active'><img src='/imgs/gallery/"+file+"' class='d-block w-100'></div>"
first_html+= "</ol>"
sec_html+="</div>"

output = first_html+sec_html

f = open("gallery.html", "w")
f.write(output)
f.close()