def capitalize_first_letter_only(s):
    def capitalize_word(word):
        if not word:
            return ''
        first_char = word[0].upper()
        rest_of_word = word[1:]
        return first_char + rest_of_word

    words = s.split()
    capitalized_words = [capitalize_word(word) for word in words]
    return ' '.join(capitalized_words)

if __name__ == '__main__':
    sample_input = "the quick brown fox jumps over the lazy dog"
    result = capitalize_first_letter_only(sample_input)
    print(result)