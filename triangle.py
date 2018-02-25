import argparse

parser = argparse.ArgumentParser(description='Lets check the type of a given triangle')

parser.add_argument('a',  help='Length of the first side', metavar='Int', type=int, default=1)
parser.add_argument('b',  help='Length of the second side', metavar='Int', type=int, default=1)
parser.add_argument('c',  help='Length of the third side', metavar='Int', type=int, default=1)

args = parser.parse_args()

if args.a == args.b == args.c:
    print ('равносторонний')
elif (args.a == args.b and args.b !=args.c) or (args.a == args.c and args.c != args.b) or (args.b == args.c and args.c != args.a):
    print ('равнобедренный')
else:
    print ('разносторонний')
