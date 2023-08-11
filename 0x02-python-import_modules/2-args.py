#!/usr/bin/python3
import sys
def main(argv):
    total = 0

    for arg in argv:
        total += int(arg)
    print(total)

if __name__ == "__main__":
    main(sys.argv[1:])
