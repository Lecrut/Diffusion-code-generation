import sys
def main():
    text = "Hello World Python Programming"
    result = [word[0] for word in text.split() if len(word) > 0]
    print("".join(result))
if __name__ == '__main__':
    main()