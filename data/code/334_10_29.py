import sys
def main():
    word1 = "hello"
    word2 = "world"
    if not word1 or not word2:
        print("Error: Both words must be non-empty.")
        return 1
    concatenated_word = f"{word1}{word2}"
    print(concatenated_word)
    return 0
if __name__ == '__main__':
    sys.exit(main())