import sys
def main():
    word1 = "Hello"
    word2 = "World"
    if len(word1) == 0 and len(word2) == 0:
        print("Error: Both words are empty.")
        return 1
    result = f"{word1}{word2}"
    print(result)
if __name__ == "__main__":
    sys.exit(main())