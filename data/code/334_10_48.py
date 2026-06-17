import sys
def main():
    word1 = "hello"
    word2 = "world"
    if not word1:
        print("Error: First word cannot be empty.")
        return 1
    elif not word2:
        print("Error: Second word cannot be empty.")
        return 1
    result = f"{word1}{word2}"
    print(result)
    sys.exit(0)
if __name__ == '__main__':
    main()