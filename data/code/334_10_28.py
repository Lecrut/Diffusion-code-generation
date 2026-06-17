import sys
def main():
    word1 = "hello"
    word2 = "world"
    if not word1:
        print("Error: First word is empty.")
        return 1
    elif not word2:
        print("Error: Second word is empty.")
        return 1
    result = f"{word1}{word2}"
    print(result)
if __name__ == "__main__":
    sys.exit(main())