def interleave_strings(str1: str, str2: str) -> str:
    return ''.join(map(lambda x, y: x + y, str1, str2))

if __name__ == '__main__':
    sample_values = {
        'str1': 'hello',
        'str2': 'world'
    }
    result = interleave_strings(sample_values['str1'], sample_values['str2'])
    print(result)