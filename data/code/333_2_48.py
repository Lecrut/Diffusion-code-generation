import sys
def main():
    sentences = [
        "Hello World",
        "Python is awesome"
    ]
    for sentence in sentences:
        words = sentence.split()
        if not words:
            continue
        first_letters = ''.join(word[0] for word in words)
        print(first_letters)
if __name__ == '__main__':
    main()