import sys
def main():
    word1 = "Hello"
    word2 = "World"
    if not word1:
        print("Error: First word is empty.")
        return 1
    if not word2:
        print("Error: Second word is empty.")
        return 1
    result = word1 + word2
    print(result)
if __name__ == '__main__':
    sys.exit(main())