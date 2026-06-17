import sys
def main():
    word1 = "Hello"
    word2 = "World"
    try:
        combined = f"{word1} {word2}"
        print(combined)
    except Exception as e:
        sys.exit(1)
if __name__ == '__main__':
    main()