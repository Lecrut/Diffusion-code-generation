def extract_digits(s):
    return [c for c in s if c.isdigit()]

if __name__ == '__main__':
    sample_strings = [
        'abc123def456',
        'no_digits_here',
        '1a2b3c',
        '999',
        '',
        'a!@#$%^&*()12345'
    ]
    for sample in sample_strings:
        result = extract_digits(sample)
        print(result)