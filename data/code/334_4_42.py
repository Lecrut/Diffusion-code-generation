import sys
def main():
    word1 = "hello"
    word2 = "world"
    print(f"{word1} {word2}")
if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"Error occurred: {e}", file=sys.stderr)
        sys.exit(1)