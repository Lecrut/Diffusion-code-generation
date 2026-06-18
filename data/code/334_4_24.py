import sys
def main():
    word1 = "Hello"
    word2 = "World"
    try:
        result = f"{word1} {word2}"
        print(result)
    except Exception as e:
        print(f"Error occurred: {e}", file=sys.stderr)
        sys.exit(1)
if __name__ == '__main__':
    main()