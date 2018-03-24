from __future__ import print_function
import sys
import xml.etree.ElementTree as etree
import time

def main():
    sys.stderr.write('Hello OSM\n')
    count = 0

    xml = open("washington-latest.osm", "r")
    for event, elem in etree.iterparse(xml):
        count += 1

        if elem.tag == 'way':
            print(elem.tag, elem.attrib)

        if count % 10000 == 0:
            sys.stderr.write('{0}\n'.format(count))

    sys.stderr.write('Parsed {0} elements'.format(count))



if __name__ == "__main__":
    main()
