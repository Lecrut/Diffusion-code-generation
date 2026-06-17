import sys
def main():
    word1 = "Hello"
    word2 = "World"
    if not isinstance(word1, str) or not isinstance(word2, str):
        print("Error: Both inputs must be strings.")
        return 1
    result = f"{word1} {word2}"
    print(result)
    return 0
if __name__ == '__main__':
    sys.exit(main())