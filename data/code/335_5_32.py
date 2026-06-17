import sys
def main():
    sentence = "Hello world from Python"
    words = sentence.split()
    print(" ".join(words))
if __name__ == '__main__':
    try:
        main()
        sys.exit(0)
    except Exception as e:
        sys.stderr.write(str(e))
        sys.exit(1)