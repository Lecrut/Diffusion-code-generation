def count_word_frequency(text):
    if not text:
        return {}
    words = text.split()
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency

if __name__ == '__main__':
    sample_text1 = "This is a sample sentence for testing."
    sample_text2 = "Another test case with multiple words."
    sample_text3 = ""
    sample_text4 = "  leading and trailing spaces are handled correctly."

    result1 = count_word_frequency(sample_text1)
    print(f"Text 1: '{sample_text1}'")
    print("Word frequency:", result1, "\n")

    result2 = count_word_frequency(sample_text2)
    print(f"Text 2: '{sample_text2}'")
    print("Word frequency:", result2, "\n")