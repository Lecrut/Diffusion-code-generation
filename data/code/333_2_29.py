import sys
def main():
    sentence = "Hello world this is a test"
    result = []
    for word in sentence.split():
        if word:
            first_letter = word[0]
            result.append(first_letter)
    print("".join(result))
if __name__ == '__main__':
    main()