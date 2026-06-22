def capitalize_first_letters(strings):
    return [s[:1].upper() + s[1:] if s else '' for s in strings]

if __name__ == '__main__':
    sample_list = ['hello', 'world', 'python', 'programming', '']
    print(capitalize_first_letters(sample_list))