import sys
def main():
    sentence = "Hello World Python Programming"
    words = sentence.split()
    first_letters = [word[0] for word in words if word]
    print("".join(first_letters))
if __name__ == '__main__':
    main()