import sys
def main():
    text = "Hello world from Python this is a test string."
    words = text.split()
    print(f"Original: {text}")
    print(f"Split result ({len(words)} items):")
    for i, word in enumerate(words, 1):
        print(f"{i}. '{word}'")
if __name__ == '__main__':
    main()