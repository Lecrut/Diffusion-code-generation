import sys
def main():
    word1 = "Hello"
    word2 = "World"
    if not word1 or not word2:
        print("Error: Both words must be non-empty.")
        return 1
    result = word1 + word2
    print(result)
    return 0
if __name__ == '__main__':
    sys.exit(main())