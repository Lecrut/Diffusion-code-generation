def count_words(text):
    if not text:
        return 0
    words = text.split()
    return len(words)

if __name__ == '__main__':
    sample_text1 = "This is a sample sentence for testing the word counter."
    sample_text2 = "Another test case with different spacing and punctuation."
    sample_text3 = ""
    sample_text4 = "Word one. Word two! Three."
    print(f"Text 1: '{sample_text1}'")
    print(f"Word count: {count_words(sample_text1)}\n")
    print(f"Text 2: '{sample_text2}'")
    print(f"Word count: {count_words(sample_text2)}\n")
    print(f"Text 3: '{sample_text3}'")
    print(f"Word count: {count_words(sample_text3)}\n")
    print(f"Text 4: '{sample_text4}'")
    print(f"Word count: {count_words(sample_text4)}\n")