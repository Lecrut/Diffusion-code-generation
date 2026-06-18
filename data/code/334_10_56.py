import sys
def main():
    word1 = "Hello"
    word2 = "World"
    if len(word1) == 0:
        print("Error: First word cannot be empty.")
        return
    if len(word2) == 0:
        print("Error: Second word cannot be empty.")
        return
    result = word1 + word2
    print(result)
if __name__ == '__main__':
    main()