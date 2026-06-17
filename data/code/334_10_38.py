import sys
def main():
    word1 = "hello"
    word2 = "world"
    if not word1:
        print("Error: First word is empty.")
        return 1
    if not word2:
        print("Error: Second word is empty.")
        return 1
    concatenated_word = word1 + "_" + word2
    print(concatenated_word)
if __name__ == '__main__':
    exit(main())