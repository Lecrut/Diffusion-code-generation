def retrieve_penultimate_element(values: list[int]) -> int:
    count = len(values)
    if count < 2:
        raise IndexError("List must contain at least two elements")
    return values[count - 2]

if __name__ == '__main__':
    test_cases = [
        [1, 2, 3, 4, 5],
        [100, 200],
        [42, 17, 99, 8],
    ]
    
    for case in test_cases:
        output = retrieve_penultimate_element(case)
        print(output)
    
    try:
        retrieve_penultimate_element([1])
    except IndexError as err:
        print(err)