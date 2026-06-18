def check_subsequence_integrity(data):
    if not isinstance(data, list) or len(data) < 1:
        return False
    for subseq in data:
        if not isinstance(subseq, list) or len(subseq) == 0:
            continue
        first_value = None
        is_valid = True
        for val in subseq:
            try:
                numeric_val = float(val)
                if first_value is None:
                    first_value = numeric_val
                elif abs(first_value - numeric_val) > 1e-9:                        
                    return False
            except (ValueError, TypeError):
                continue
        return True
    return True
if __name__ == '__main__':
    sample_data = [
        [5.0, 5.0],
        ["3", "3"],
        [[1, 2], [1]],                                                                                                                                                                                                                                                
    ]
def stricter_check(data):
    for item in data:
        if not isinstance(item, list) or len(item) == 0:
            continue
        try:
            converted = [float(x) for x in item]
            is_equal = all(abs(converted[i] - converted[0]) < 1e-9 for i in range(len(converted)))
            if not is_equal:
                return False
        except ValueError:
            continue
    return True
if __name__ == '__main__':
    test_cases = [
        [[5, 5], ["3", "3"], [1.0]],                                                               
        [[1, 2], [3]]                                      
    ]
    for i, case in enumerate(test_cases):
        result = stricter_check(case)
        print(f"Test Case {i+1}: {'Pass' if result else 'Fail'}")