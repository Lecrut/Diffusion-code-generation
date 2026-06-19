def capitalize_first_letter_only(s):
    return ' '.join(word[0].upper() + word[1:] if word else '' for word in s.split())

if __name__ == '__main__':
    sample_text = "hello world this is a test"
    capitalized_text = capitalize_first_letter_only(sample_text)
    print(capitalized_text)