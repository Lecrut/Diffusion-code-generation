def reverse_words(text):
    return ' '.join(text.split()[::-1])

if __name__ == '__main__':
    sample_string1 = "hello world this is a test"
    print(f"Input: '{sample_string1}'")
    print(f"Output: '{reverse_words(sample_string1)}'")
    
    sample_string2 = "optimization is key"
    print(f"Input: '{sample_string2}'")
    print(f"Output: '{reverse_words(sample_string2)}'")
    
    sample_string3 = "  leading and trailing spaces   "
    print(f"Input: '{sample_string3}'")
    print(f"Output: '{reverse_words(sample_string3)}'")