def concatenate_strings(str1: str, str2: str) -> str:
    return str1 + str2

if __name__ == '__main__':
    sample_values = {
        'greeting': 'hello',
        'target': 'world'
    }
    
    result = concatenate_strings(sample_values['greeting'], sample_values['target'])
    print(result)