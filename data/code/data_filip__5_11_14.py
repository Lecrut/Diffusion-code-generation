def capitalize_strings(input_tuple):
    return tuple(s[0].upper() + s[1:].lower() if s else '' for s in input_tuple)

if __name__ == '__main__':
    sample_input = ('hElLo', 'wOrLd', 'pYtHoN', 'TeSt', 'a', '', 'AbCdEf')
    result = capitalize_strings(sample_input)
    print(result)