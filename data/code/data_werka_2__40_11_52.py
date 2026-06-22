def first_letter(s):
    if s:
        return s[0]
    else:
        return ''

if __name__ == '__main__':
    sample_values = ["Hello", "", "World", "Python"]
    for value in sample_values:
        print(first_letter(value))