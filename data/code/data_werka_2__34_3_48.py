def capitalize_first_letter(s):
    def capitalize(word):
        return word[0].upper() + word[1:] if word else ''

    words = s.split()
    capitalized_words = [capitalize(word) for word in words]
    return ' '.join(capitalized_words)

if __name__ == '__main__':
    sample_string = "this is a test string with multiple words"
    result = capitalize_first_letter(sample_string)
    print(result)