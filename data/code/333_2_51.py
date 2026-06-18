import sys
def main():
    sentence = "Hello World This is a Test"
    words = sentence.split()
    first_letters = [word[0] for word in words if len(word) > 0]
    print("".join(first_letters))
if __name__ == '__main__':
    sys.exit(main())