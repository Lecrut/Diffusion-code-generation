import sys
def main():
    sentence = "Hello world this is a test command line utility"
    words = sentence.split()
    print(" ".join(words))
if __name__ == '__main__':
    main()
sys.exit(0)