import sys
def main():
    text = "Hello world! This is a test string."
    words = [word.strip() for word in text.split()]
    if not words:
        print("No words found.")
        return 0
    longest_word = max(words, key=len)
    sorted_words = sorted(words, reverse=True)
    result_str = " ".join(sorted_words[1:])
    output_text = f"Original text processed.\nLongest word: {longest_word}\nSorted words (excluding first): {result_str}"
    print(output_text)
    return 0
if __name__ == '__main__':
    sys.exit(main())