def capitalize_first_letter(s):
    words = s.split()
    capitalized_words = [word[0].upper() + word[1:] for word in words]
    return ' '.join(capitalized_words)

if __name__ == '__main__':
    sample_string = "welcome to the future of computing"
    result = capitalize_first_letter(sample_string)
    print(result)