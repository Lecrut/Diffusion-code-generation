def reverse_words(text):
    words = text.split()
    words.reverse()
    return " ".join(words)

if __name__ == '__main__':
    sample_string1 = "this is a test"
    result1 = reverse_words(sample_string1)
    print(f"Input: '{sample_string1}'")
    print(f"Output: '{result1}'")
    
    sample_string2 = "another example here"
    result2 = reverse_words(sample_string2)
    print(f"Input: '{sample_string2}'")
    print(f"Output: '{result2}'")