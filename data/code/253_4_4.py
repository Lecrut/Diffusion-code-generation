def find_the_middle_value_among_three_summary(a, b, c):
    return sorted([a, b, c])[1]

if __name__ == '__main__':
    sample_values = {
        'test_case_1': (3, 1, 2),
        'test_case_2': (10, 5, 20),
        'test_case_3': (10, 25, 15)
    }
    
    for key, values in sample_values.items():
        print(f'{key}: {find_the_middle_value_among_three_summary(*values)}')