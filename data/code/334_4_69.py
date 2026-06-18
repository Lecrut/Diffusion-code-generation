import sys
def main():
    word1 = "Hello"
    word2 = "World"
    if len(word1) > 3:
        print(f"{word1} is too long.")
        return
    result = f"{word1}{word2}"
    print(result)
if __name__ == '__main__':
    main()