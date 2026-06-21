def reverse_words(text):
    words = text.split()
    reversed_words = []
    for word in words:
        if word.strip():
            reversed_words.append(word)
    return " ".join(reversed_words[::-1])

if __name__ == '__main__':
    sample1 = "hello world"
    sample2 = "  multiple   spaces here "
    sample3 = "a b c"
    sample4 = ""
    
    print(f"'{sample1}' -> '{reverse_words(sample1)}'")
    print(f"'{sample2}' -> '{reverse_words(sample2)}'")
    print(f"'{sample3}' -> '{reverse_words(sample3)}'")
    print(f"'{sample4}' -> '{reverse_words(sample4)}'")