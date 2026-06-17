import sys
def main():
    word1 = "Hello"
    word2 = "World"
    concatenated = f"{word1}{word2}"
    if not word1:
        print("First word is empty.")
        return 1
    if not word2:
        print("Second word is empty.")
        return 1
    print(concatenated)
if __name__ == '__main__':
    sys.exit(main())