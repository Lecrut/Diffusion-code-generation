def compute_square_perimeter(side_length):
    if side_length < 0:
        raise ValueError('Side length cannot be negative')
    return 4 * side_length

if __name__ == '__main__':
    test_cases = {
        'test_1': {'input': 0, 'expected': 0},
        'test_2': {'input': 1, 'expected': 4},
        'test_3': {'input': 2.5, 'expected': 10},
        'test_4': {'input': 10, 'expected': 40}
    }
    
    for test_name, test_data in test_cases.items():
        result = compute_square_perimeter(test_data['input'])
        assert result == test_data['expected'], f'{test_name} failed: input({test_data["input"]}) => output({result}), expected({test_data["expected"]})'
    
    sample_side_length = 5
    perimeter = compute_square_perimeter(sample_side_length)
    print(perimeter)