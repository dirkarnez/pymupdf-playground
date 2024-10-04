doc = pymupdf.open("output.pdf")  # re-open PDF
page = doc[0]  # first page
page.get_drawings()  # extract its drawings

# Out[14]:
# [{
# 'items': [  # draw commands are here
#   ('re', Rect(100.0, 100.0, 200.0, 200.0), 1),  # rect from above
#   ('l', Point(100.0, 200.0), Point(200.0, 100.0)),  # first line
#   ('l', Point(200.0, 200.0), Point(100.0, 100.0)),  # second line
# ],
# 'closePath': True,  # whether to connect first & last points
# 'type': 'fs',  # a fill & stroke path
# 'stroke_opacity': 1.0,  # no border opacity
# 'color': (1.0, 0.0, 0.0),  # border color
# 'width': 1.5,  # line width
# 'lineCap': (0, 0, 0),  # line end format
# 'lineJoin': 0.0,  # line join format
# 'dashes': '[] 0',  # line dashing pattern 
# 'rect': Rect(100.0, 100.0, 200.0, 200.0),  # the original rectangle
# 'seqno': 1,  # first rendering action on page
# 'even_odd': False,  # how intersecting areas are colored
# 'fill_opacity': 1.0,  # no fill opacity
# 'fill': (1.0, 1.0, 0.0),  # fill color yellow
# }]
