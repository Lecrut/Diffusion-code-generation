def capitalize_first_letter(s):
    words = s.split()
    capitalized_words = [word[0].upper() + word[1:] if word else '' for word in words]
    return ' '.join(capitalized_words)

if __name__ == '__main__':
    sample_string = "another example with different words"
    capitalized_string = capitalize_first_letter(sample_string)
    print(capitalized_string)