import sys
def main():
    word1 = "Hello"
    word2 = "World"
    if len(word1) > 5:
        print(f"{word1} is too long.")
        return
    combined = f"{word1}-{word2}"
    print(combined)
if __name__ == '__main__':
    main()