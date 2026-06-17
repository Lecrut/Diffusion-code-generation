import sys
def main():
    word1 = "Hello"
    word2 = "World"
    if len(word1) == 0 and len(word2) == 0:
        print("Error: Both words must be non-empty.")
        sys.exit(1)
    result = word1 + word2
    print(result)
if __name__ == '__main__':
    main()