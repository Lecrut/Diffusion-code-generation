import sys
def main():
    word1 = "hello"
    word2 = "world"
    if not word1 or not word2:
        print("Error: Both words must be non-empty.")
        sys.exit(1)
    result = word1 + word2
    print(result)
if __name__ == '__main__':
    main()