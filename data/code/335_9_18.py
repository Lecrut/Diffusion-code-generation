import sys
def main():
    text = "Hello world! This is a Pythonic example."
    words = text.split()
    print(f"Original: {text}")
    print(f"Split result ({len(words)} items):")
    for i, word in enumerate(words, 1):
        print(f"{i}. '{word}'")
if __name__ == '__main__':
    try:
        main()
        sys.exit(0)
    except Exception as e:
        print(f"Error occurred: {e}", file=sys.stderr)
        sys.exit(1)