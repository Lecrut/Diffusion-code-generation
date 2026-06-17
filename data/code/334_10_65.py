import sys
def main():
    word1 = "Hello"
    word2 = "World"
    if not word1 or not word2:
        print("Error: Both words must be non-empty.")
        return 1
    concatenated_word = f"{word1}{word2}"
    print(concatenated_word)
if __name__ == '__main__':
    exit(main())