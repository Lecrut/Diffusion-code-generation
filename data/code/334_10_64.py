def main():
    word1 = "Hello"
    word2 = "World"
    if not word1:
        print("Error: First word cannot be empty.")
        return 1
    if not word2:
        print("Error: Second word cannot be empty.")
        result_word = f"{word1}{word2}"
        print(result_word)
if __name__ == '__main__':
    main()