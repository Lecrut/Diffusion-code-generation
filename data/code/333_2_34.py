import sys
def main():
    sentence = "Hello world this is a test"
    result_chars = [word[0] for word in sentence.split() if word]
    print("".join(result_chars))
if __name__ == '__main__':
    main()