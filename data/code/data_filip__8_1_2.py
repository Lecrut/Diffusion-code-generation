def split_csv(csv_string):
    if not csv_string:
        return []
    segments = csv_string.split(',')
    meaningful = [seg for seg in segments if seg]
    return meaningful
if __name__ == '__main__':
    test_cases = ['apple,banana,cherry', 'one,,three,,five', ',,,,,,', 'single', '  spaces  , around , commas  ', '', 'a,b,c,d,e', 'trailing,', ',leading']
    for test in test_cases:
        result = split_csv(test)
        print(f"Input: '{test}' -> Output: {result}")