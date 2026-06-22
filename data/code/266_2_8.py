def count_word_frequency(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string.")
    
    word_count = {}
    words = text.split()
    for word in words:
        word = word.strip().lower()
        if word:
            word_count[word] = word_count.get(word, 0) + 1
    return word_count

if __name__ == '__main__':
    sample_text1 = "This is a sample sentence for testing."
    sample_text2 = "Another test case with multiple words."
    sample_text3 = ""
    sample_text4 = "   leading and trailing spaces are handled correctly."

    print(f"Text 1: '{sample_text1}'")
    print(f"Word frequency: {count_word_frequency(sample_text1)}\n")

    print(f"Text 2: '{sample_text2}'")
    print(f"Word frequency: {count_word_frequency(sample_text2)}\n")

    try:
        print(f"Text 3: '{sample_text3}'")
        print(f"Word frequency: {count_word_frequency(sample_text3)}\n")
    except ValueError as e:
        print(e)

    print(f"Text 4: '{sample_text4}'")
    print(f"Word frequency: {count_word_frequency(sample_text4)}\n")