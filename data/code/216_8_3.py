def find_middle(data):
    n = len(data)
    if n == 0:
        raise ValueError("List is empty")
    middle_index = n // 2
    return data[middle_index]
def test_find_middle():
    test_cases = [
        ([1, 2, 3, 4, 5], 3),
        ([10, 20, 30], 20),
        ([7], 7),
        ([], None)                                                                                 
    ]
    for input_list, expected in test_cases:
        try:
            result = find_middle(input_list)
            if result == expected:
                print(f"PASS: Input {input_list}, Expected {expected}, Got {result}")
            else:
                print(f"FAIL: Input {input_list}, Expected {expected}, Got {result}")
        except ValueError as e:
            if expected is None:
                print(f"PASS: Input {input_list}, Caught expected error: {e}")
            else:
                print(f"FAIL: Input {input_list}, Unexpected error: {e}")
        except Exception as e:
            print(f"ERROR: Input {input_list} raised unexpected exception: {e}")
if __name__ == '__main__':
    test_find_middle()