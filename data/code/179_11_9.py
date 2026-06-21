def reverse_words(text):
    words = text.split()
    reversed_words = words[::-1]
    return " ".join(reversed_words)

if __name__ == '__main__':
    sample_string1 = "Python is fun"
    result1 = reverse_words(sample_string1)
    print(f"Input: '{sample_string1}'")
    print(f"Output: '{result1}'")

    sample_string2 = "coding challenges are exciting"
    result2 = reverse_words(sample_string2)
    print(f"Input: '{sample_string2}'")
    print(f"Output: '{result2}'")

    sample_string3 = "  extra   spaces    everywhere "
    result3 = reverse_words(sample_string3)
    print(f"Input: '{sample_string3}'")
    print(f"Output: '{result3}'")