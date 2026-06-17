import sys
def main():
    word1 = "hello"
    word2 = "world"
    combined_string = f"{word1} {word2}"
    print(combined_string)
if __name__ == '__main__':
    try:
        main()
        sys.exit(0)
    except Exception as e:
        print(f"Error occurred: {e}", file=sys.stderr)
        sys.exit(1)