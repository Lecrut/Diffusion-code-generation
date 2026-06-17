import sys
def main():
    word1 = "Hello"
    word2 = "World"
    if len(word1) < 3:
        print("Error: First word must be at least three characters long.")
        return 1
    combined_string = f"{word1} {word2}".upper()
    print(combined_string)
    return 0
if __name__ == '__main__':
    sys.exit(main())