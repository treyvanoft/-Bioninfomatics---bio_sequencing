from bioseq.calculation.SeqCal import gcContent, countBasesDict,countBasesDict_re
from bioseq.pattern.SeqPattern import cpgSearch,transcription,transcription_re,translation,translation_re,enzTargetsScan,enzTargetsScan_re
# print("in Main.py")

def argparserLocal():
    from argparse import ArgumentParser
    '''Argument parser for the commands'''
    parser = ArgumentParser(prog='myseq', description='Work with sequence')

    subparsers = parser.add_subparsers(
        title='commands', description='Please choose command below:',
        dest='command'
    )
    subparsers.required = True

    cgc_command = subparsers.add_parser('gcContent', help='Calculate GC content')
    cgc_command.add_argument("-s", "--seq", type=str, default=None, dest='seq',
                             help="Provide sequence")
 

    count_command = subparsers.add_parser('countBases', help='Count number of each base')
    count_command.add_argument("-s", "--seq", type=str, default=None,
                             help="Provide sequence")
    count_command.add_argument("-r", "--revcomp",  action='store_true', default=None,
                             help="Convet DNA to reverse-complementary")


    cgcserch_command = subparsers.add_parser('cpgScan', help='Search for CpG sequence')
    cgcserch_command.add_argument("-s", "--seq", type=str, default=None,
                             help="Provide sequence")

    
    enzTargetsScan_command = subparsers.add_parser('enzTargetsScan', help='Search for Enzyme ')
    enzTargetsScan_command.add_argument("-s", "--seq", type=str, default=None,
                             help="Provide sequence")
    enzTargetsScan_command.add_argument("-e", "--enz", type=str, default=None,
                             help="Enzyme name")
    enzTargetsScan_command.add_argument("-r", "--revcomp", action='store_true',  default=None,
                             help="Convet DNA to reverse-complementary")
    
    
    transcription_command = subparsers.add_parser('transcription', help='transcription DNA TO RNA')
    transcription_command.add_argument("-s", "--seq", type=str, default=None,
                             help="Provide sequence")
    transcription_command.add_argument("-r", "--revcomp", action='store_true',  default=None,
                             help="Convet DNA to reverse-complementary")
    
    
    translation_command = subparsers.add_parser('translation', help='translation DNA TO Protein')
    translation_command.add_argument("-s", "--seq", type=str, default=None,
                             help="Provide sequence")
    translation_command.add_argument("-r", "--revcomp", action='store_true',  default=None,
                             help="Convet DNA to reverse-complementary")
    
    
    
    
 
    return parser
    
def main():
    parser = argparserLocal()
    args = parser.parse_args()


    if args.command == 'gcContent':
        if args.seq == None:
            exit(parser.parse_args(['gcContent','-h']))
        seq = args.seq.upper()
        print("Input",args.seq,"\nGC content =", gcContent(seq) )

    elif args.command == 'countBases':
        if args.seq == None:
            exit(parser.parse_args(['countBases','-h'])) 
        if args.revcomp != None:
            seq = args.seq.upper()
            print("Input",args.seq,"\ncountBases =", countBasesDict_re(seq) ) 
        else: 
            seq = args.seq.upper()
            print("Input",args.seq,"\ncountBases =", countBasesDict(seq) )

    elif args.command == 'cpgScan':
        if args.seq == None:
            exit(parser.parse_args(['cpgScan','-h']))
        seq = args.seq.upper()
        print("Input",args.seq,"\ncpgScan =", cpgSearch(seq) )  
    
    elif args.command == 'enzTargetsScan':
        if args.seq == None:
            exit(parser.parse_args(['enzTargetsScan','-h']))
        if args.enz == None:
            exit(parser.parse_args(['enzTargetsScan','-h']))
        if args.revcomp != None:
            seq = args.seq.upper()
            enz = args.enz;
            print("Input",args.seq,"\nenzTargetsScan =", enzTargetsScan_re(seq,enz) ) 
        else: 
            seq = args.seq.upper()
            enz = args.enz;
            print("Input",args.seq,"\nenzTargetsScan =", enzTargetsScan(seq,enz) )  
       
    
    elif args.command == 'transcription':
        if args.seq == None:
            exit(parser.parse_args(['transcription','-h']))
        if args.revcomp != None:
            seq = args.seq.upper()
            print("Input",args.seq,"\ntranscription =", transcription_re(seq) ) 
        else: 
            seq = args.seq.upper()
            print("Input",args.seq,"\ntranscription =", transcription(seq) )  
        
    elif args.command == 'translation':
        if args.seq == None:
            exit(parser.parse_args(['translation','-h']))
        if args.revcomp != None:
            seq = args.seq.upper()
            print("Input",args.seq,"\ntranslation =", translation_re(seq) ) 
        else: 
            seq = args.seq.upper()
            print("Input",args.seq,"\ntranslation =", translation(seq) )  

# print(__name__)
if __name__ == "__main__":   
       main()



