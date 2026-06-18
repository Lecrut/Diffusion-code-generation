import sys
def main():
    word1 = "hello"
    word2 = "world"
    if not word1:
        print("First word is empty.")
        return 1
    if not word2:
        print("Second word is empty.")
        return 1
    concatenated_word = f"{word1}{word2}"
    print(concatenated_word)
if __name__ == "__main__":
    sys.exit(main())