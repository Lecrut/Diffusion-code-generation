import sys
def main():
    word1 = "Hello"
    word2 = "World"
    result = f"{word1} {word2}"
    print(result)
if __name__ == '__main__':
    try:
        main()
        sys.exit(0)
    except Exception as e:
        print(f"Error occurred: {e}", file=sys.stderr)
        sys.exit(1)