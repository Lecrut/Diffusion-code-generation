def substring_in_text(substring, text):
    return text.find(substring) != -1

if __name__ == '__main__':
    sample_substring = "example"
    sample_text = "This is an example text for testing."
    print(substring_in_text(sample_substring, sample_text))