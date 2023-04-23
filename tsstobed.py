from optparse import OptionParser
parser = OptionParser()
parser.add_option("-i", "--filein", dest="filein",
                  help="file with tabled TSS from base", metavar="FILE")
parser.add_option("-o", "--fileout", dest="fileout",
                  help="name of the output file", metavar="FILE")

(options, args) = parser.parse_args()

print(options.filein, options.fileout)