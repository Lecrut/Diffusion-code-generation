import sys
def main():
    word1 = "hello"
    word2 = "world"
    if not (word1 and word2):
        print("Error: Both words must be provided.")
        return 1
    result = f"{word1} {word2}"
    print(result)
    return 0
if __name__ == '__main__':
    sys.exit(main())