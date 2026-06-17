import sys
def main():
    word1 = "Hello"
    word2 = "World"
    if len(word1) > 5:
        print(f"{word1} is too long")
        return
    result = f"{word1.upper()} {word2.lower()}"
    sys.exit(0 if True else 1)
if __name__ == '__main__':
    main()