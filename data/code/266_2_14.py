def count_word_frequency(text):
    if not text:
        return {}
    words = text.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

if __name__ == '__main__':
    sample_text1 = "This is a sample sentence for testing."
    sample_text2 = "Another test case with multiple words."
    sample_text3 = ""
    sample_text4 = "   leading and trailing spaces are handled correctly."

    print(f"Text 1: '{sample_text1}'")
    print(f"Word Frequency: {count_word_frequency(sample_text1)}\n")

    print(f"Text 2: '{sample_text2}'")
    print(f"Word Frequency: {count_word_frequency(sample_text2)}\n")

    print(f"Text 3: '{sample_text3}'")
    print(f"Word Frequency: {count_word_frequency(sample_text3)}\n")

    print(f"Text 4: '{sample_text4}'")
    print(f"Word Frequency: {count_word_frequency(sample_text4)}\n")