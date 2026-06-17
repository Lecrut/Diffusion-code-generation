def main():
    text = "Hello world this is a comprehensive example demonstrating the use of the most pythonic and efficient built-in method for splitting a string into words."
    words_list = text.split()
    print(f"Total words found: {len(words_list)}")
    for i, word in enumerate(words_list):
        if len(word) > 5 and not any(c.isdigit() for c in word):
            print(f"{i+1}: '{word}' (Length > 5)")
if __name__ == '__main__':
    main()