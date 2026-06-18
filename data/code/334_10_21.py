import sys
def main():
    word1 = "hello"
    word2 = "world"
    if len(word1) == 0 and len(word2) == 0:
        print("Error: Both words are empty.")
        sys.exit(1)
    result = f"{word1}{word2}"
    print(result)
if __name__ == '__main__':
    main()