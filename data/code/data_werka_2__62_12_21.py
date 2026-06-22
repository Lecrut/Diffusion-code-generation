my_list = [10, 20, 30, 40]

def fetch_second_element(lst):
    return lst[1] if len(lst) > 1 else None

if __name__ == '__main__':
    second_element = fetch_second_element(my_list)
    print(second_element)

    # Additional test cases
    test_cases = {
        'short_list': [5, 15],
        'single_element_list': [7],
        'empty_list': []
    }

    for name, lst in test_cases.items():
        result = fetch_second_element(lst)
        print(f"{name}: {result}")