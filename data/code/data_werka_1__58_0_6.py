def retrieve_first_element(elements):
    return elements[0]

if __name__ == '__main__':
    test_cases = {
        'case1': [5, 10, 15],
        'case2': ['a', 'b', 'c'],
        'case3': [True, False, True]
    }
    
    for case_name, sample_list in test_cases.items():
        first_element = retrieve_first_element(sample_list)
        print(f"First element of {case_name}: {first_element}")