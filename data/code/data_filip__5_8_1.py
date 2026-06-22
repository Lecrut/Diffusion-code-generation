def capitalize_first_letter(text):
    if not text:
        return text
    return text[0].upper() + text[1:]

if __name__ == '__main__':
    result1 = capitalize_first_letter('hello world')
    print(result1)

    result2 = capitalize_first_letter('already Capitalized')
    print(result2)

    result3 = capitalize_first_letter('')
    print(result3)

    result4 = capitalize_first_letter('a')
    print(result4)

    assert result1 == 'Hello world'
    assert result2 == 'Already Capitalized'
    assert result3 == ''
    assert result4 == 'A'