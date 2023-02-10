#!/usr/bin/python3
"""
    Parsing bold syntax
"""
if __name__ == "__main__":
    import sys
    from os import path
    import re
    import hashlib

    markD = {"#": "h1", "##": "h2", "###": "h3", "####": "h4",
             "#####": "h5", "######": "h6", "-": "ul", "*": "ol"}

    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        exit(1)

    if not path.exists(sys.argv[1]) or not str(sys.argv[1]).endswith(".md"):
        sys.stderr.write("Missing " + sys.argv[1] + '\n')
        exit(1)

    def handleHeadings(pattern):
        tag = markD[lineSplit[0]]
        toWrite = line.replace("{} ".format(lineSplit[0]), "<{}>".format(tag))
        toWrite = toWrite[:-1] + ("</{}>\n".format(tag))
        fw.write(toWrite)
