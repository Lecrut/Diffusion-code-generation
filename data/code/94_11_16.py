def is_any_true(data, bool_list):
    return data or any(bool_list)

if __name__ == '__main__':
    result1 = is_any_true(True, [False, False])
    result2 = is_any_true(False, [True, True])
    result3 = is_any_true(False, [False, False, True])
    result4 = is_any_true(False, [])
    
    print(f"Result 1: {result1}")
    print(f"Result 2: {result2}")
    print(f"Result 3: {result3}")
    print(f"Result 4: {result4}")