import sys
def main():
    text = "Hello world! This is a test string."
    words_list = text.split()
    print(f"Original: {text}")
    print(f"Split result ({len(words_list)} items):")
    for i, word in enumerate(words_list, 1):
        clean_word = ''.join(c.lower() for c in word if not (c.isalpha())) or '' 
        print(f"{i}. '{word}' -> '{clean_word}'")
if __name__ == '__main__':
    main()