import sys
def main():
    sentence = "Hello World Python Programming"
    words = sentence.split()
    if not words:
        print("")
        return
    result = "".join(word[0] for word in words)
    print(result)
if __name__ == '__main__':
    main()