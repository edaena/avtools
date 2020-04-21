#!/usr/bin/python
# Parse caption files generated with Adobe Premiere Pro CC 2019
import os
import sys
import xml.etree.ElementTree as ET

dir = sys.argv[1]
out_dir = sys.argv[2]
print(dir)

files = os.listdir(dir)

for file in files:
    if not file.endswith('.xml'):
        continue
    xml_file = os.path.join(dir, file)
    text_file = os.path.join(out_dir, file.replace('.xml', '.txt'))
    f = open(text_file, 'w', encoding='utf-8')

    tree = ET.parse(xml_file)
    root = tree.getroot()
    body = root.findall('{http://www.w3.org/ns/ttml}body')
    div = body[0].findall('{http://www.w3.org/ns/ttml}div')
    ps = div[0].findall('{http://www.w3.org/ns/ttml}p')

    for p in ps:
        span = p.findall('{http://www.w3.org/ns/ttml}span')
        f.write(span[0].text + ' ')

    f.close()
