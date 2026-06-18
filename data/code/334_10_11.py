import sys
def main():
    word1 = "hello"
    word2 = "world"
    if not word1:
        print("Error: First word cannot be empty.")
        return 0
    if not word2:
        print("Error: Second word cannot be empty.")
        return 0
    concatenated_word = f"{word1}{word2}"
    print(concatenated_word)
if __name__ == '__main__':
    sys.exit(main())