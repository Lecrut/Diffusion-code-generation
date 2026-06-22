def first_letter_of_each_word(s):
    import re
    words = re.split(r'\s+', s.strip())
    return ''.join(word[0] for word in words if word)

if __name__ == '__main__':
    sample_input = "  Hello   World! This is a Test.  "
    result = first_letter_of_each_word(sample_input)
    print(result)