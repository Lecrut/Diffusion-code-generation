def capitalize_first_letter(s):
    return ' '.join(word[0].upper() + word[1:] if word else '' for word in s.split())

if __name__ == '__main__':
    sample_string = "this is a Sample String with MiXeD CaSe."
    capitalized_string = capitalize_first_letter(sample_string)
    print(capitalized_string)