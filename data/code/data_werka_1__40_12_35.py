def get_first_letter(s):
    try:
        return s[0]
    except IndexError:
        return ''

if __name__ == '__main__':
    sample_values = ["Hello", "", "World", "Python", None, 123, []]
    for value in sample_values:
        print(get_first_letter(str(value)))