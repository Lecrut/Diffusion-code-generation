def reverse_word_order(text: str) -> str:
    words = text.split()
    words.reverse()
    return " ".join(words)

if __name__ == '__main__':
    sample_string1 = "Python is awesome"
    result1 = reverse_word_order(sample_string1)
    print(f"'{sample_string1}' -> '{result1}'")