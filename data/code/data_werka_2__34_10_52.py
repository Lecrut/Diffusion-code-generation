def capitalize_initials(s):
    return ' '.join(word.capitalize() for word in s.split())

if __name__ == '__main__':
    example_sentence = "discovering new horizons in ai research"
    capitalized_sentence = capitalize_initials(example_sentence)
    print(capitalized_sentence)