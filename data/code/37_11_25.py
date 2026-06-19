def concatenate_strings(str1, str2):
    return ''.join([str1, str2])

if __name__ == '__main__':
    sample_values = {
        'string_a': "Hello",
        'string_b': "World"
    }
    result = concatenate_strings(sample_values['string_a'], sample_values['string_b'])
    print(result)