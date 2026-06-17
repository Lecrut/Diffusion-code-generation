import sys
def main():
    text = "Hello, World! This is a Pythonic example."
    words = [word.strip() for word in text.split()]
    print(f"Original: {text}")
    print(f"Split Result ({len(words)} items):")
    for i, w in enumerate(words):
        print(f"{i + 1}. '{w}'")
if __name__ == '__main__':
    main()
sys.exit(0)