import sys
def main():
    text = "Hello world! This is a test string."
    words = text.split()
    print(f"Original Text: {text}")
    print(f"Parsed Words Count: {len(words)}")
    for i, word in enumerate(words):
        clean_word = ''.join(c.lower() if c.isalpha() else ' ' for c in word)
        words[i] = clean_word
    result_list = [word.strip('!.,;:') for word in text.split()]
    print(f"Cleaned Words: {result_list}")
if __name__ == '__main__':
    main()