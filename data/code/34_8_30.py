def capitalize_first_letter(s):
    return ' '.join(word[0].upper() + word[1:] if word else '' for word in s.split())

if __name__ == '__main__':
    sample_input = "this is a Test String with some MiXeD CaSe."
    result = capitalize_first_letter(sample_input)
    print(result)