def concatenate_strings(str1: str, str2: str) -> str:
    return f"{str1}{str2}"

if __name__ == '__main__':
    sample_values = {
        'string1': 'hello',
        'string2': 'world'
    }
    
    result = concatenate_strings(sample_values['string1'], sample_values['string2'])
    print(result)