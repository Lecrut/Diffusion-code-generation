def strip_whitespace(s):
    return s.strip()

if __name__ == '__main__':
    sample_string = "   hello world   "
    result = strip_whitespace(sample_string)
    print(result)

    another_sample = "\t\n\t\n  spaces around  \t\n\t\n"
    result2 = strip_whitespace(another_sample)
    print(result2)

    no_whitespace = "no leading or trailing whitespace"
    result3 = strip_whitespace(no_whitespace)
    print(result3)

    empty_string = "   "
    result4 = strip_whitespace(empty_string)
    print(result4)

    mixed_whitespace = " \t\r\n  content  \t\r\n "
    result5 = strip_whitespace(mixed_whitespace)
    print(result5)