def count_words(text):
    word_count = {}
    words = text.split()
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

    count1 = count_words(sample_text1)
    print(f"Text: '{sample_text1}'")
    print(f"Word Count: {count1}\n")

    count2 = count_words(sample_text2)
    print(f"Text: '{sample_text2}'")
    print(f"Word Count: {count2}\n")

    count3 = count_words(sample_text3)
    print(f"Text: '{sample_text3}'")
    print(f"Word Count: {count3}\n")

    count4 = count_words(sample_text4)
    print(f"Text: '{sample_text4}'")
    print(f"Word Count: {count4}\n")