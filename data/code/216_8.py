def find_middle(data):
    n = len(data)
    if n == 0:
        raise ValueError("List is empty")
    if n % 2 != 0:
        return data[n // 2]
    else:
        return data[n // 2 - 1]
def test_find_middle():
    test_cases = [
        ([1, 2, 3, 4, 5], 3),
        ([1, 2, 3, 4], 2),
        ([10], 10),
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
                print(f"PASS: Input {input_list}, Expected None, Caught expected error: {e}")
            else:
                print(f"FAIL: Input {input_list}, Expected {expected}, Caught unexpected error: {e}")
        except Exception as e:
            print(f"ERROR: Input {input_list} caused an unexpected exception: {e}")
if __name__ == '__main__':
    test_find_middle()