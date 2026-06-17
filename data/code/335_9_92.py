import sys
def main():
    text = "Hello world! This is a test string."
    words_list = text.split()
    print(f"Original: {text}")
    print(f"Split result ({len(words_list)} items):")
    for i, word in enumerate(words_list, 1):
        print(f"{i}. '{word}'")
if __name__ == '__main__':
    try:
        main()
        sys.exit(0)
    except Exception as e:
        sys.exit(1)