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
    concatenated_word = f"{word1}{word2}"
    print(concatenated_word)
if __name__ == '__main__':
    sys.exit(main())