import sys
def main():
    text = "Hello world! This is a Pythonic example."
    words = text.split()
    print(f"Original: {text}")
    print(f"Split result ({len(words)} items):")
    for i, word in enumerate(words):
        print(f"{i+1}. '{word}'")
if __name__ == '__main__':
    main()