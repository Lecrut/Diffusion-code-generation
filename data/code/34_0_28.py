def capitalize_first_letter(text):
    return ' '.join(word[0].upper() + word[1:] if word else '' for word in text.split())

if __name__ == '__main__':
    sample_input = "this is a Sample String with MiXeD CaSe"
    result = capitalize_first_letter(sample_input)
    print(result)