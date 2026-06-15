import string
def extract_punctuation(text):
    punctuation_set = set()
    for char in text:
        if char in string.punctuation:
            punctuation_set.add(char)
    return punctuation_set
if __name__ == '__main__':
    sample_string1 = "Hello, world! How are you?"
    sample_string2 = "This is a test string with numbers 123 and symbols @#$."
    sample_string3 = "No punctuation here."
    sample_string4 = "!@#$%^&*()_+=-`~[]{}\\|;:'\",.<>/? "
    result1 = extract_punctuation(sample_string1)
    print(f"'{sample_string1}' -> {result1}")
    result2 = extract_punctuation(sample_string2)
    print(f"'{sample_string2}' -> {result2}")
    result3 = extract_punctuation(sample_string3)
    print(f"'{sample_string3}' -> {result3}")
    result4 = extract_punctuation(sample_string4)
    print(f"'{sample_string4}' -> {result4}")