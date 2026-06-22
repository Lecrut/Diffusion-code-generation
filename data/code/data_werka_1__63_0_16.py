def retrieve_first_element(sequence):
    return sequence[0] if sequence else None

if __name__ == '__main__':
    test_cases = {
        'case1': [5, 15, 25, 35],
        'case2': ['apple', 'banana', 'cherry'],
        'case3': [True, False, True],
        'case4': [],
    }
    
    for case_name, sequence in test_cases.items():
        first_element = retrieve_first_element(sequence)
        print(f"First element of {case_name}: {first_element}")