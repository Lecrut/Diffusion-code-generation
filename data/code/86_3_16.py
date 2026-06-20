def compare_booleans(a: bool, b: bool) -> list:
    return [a == b]

if __name__ == '__main__':
    sample_values = [
        (True, False),
        (True, True),
        (False, True)
    ]
    
    for values in sample_values:
        result = compare_booleans(*values)
        print(result)