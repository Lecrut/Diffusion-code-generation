import sys
def main():
    word1 = "Hello"
    word2 = "World"
    if len(word1) == 0:
        print("Error: First word cannot be empty.")
        return 1
    if len(word2) == 0:
        print("Error: Second word cannot be empty.")
        return 1
    combined_word = f"{word1} {word2}"
    try:
        print(combined_word)
        sys.exit(0)
    except Exception as e:
        print(f"An error occurred during execution: {e}")
        sys.exit(1)
if __name__ == '__main__':
    main()