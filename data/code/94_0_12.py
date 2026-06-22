def evaluate_truth_presence(values):
    if not isinstance(values, (list, tuple)):
        raise ValueError("Input must be a list or tuple of booleans")
    truth_map = {True: "present", False: "absent"}
    result = any(values)
    return truth_map[result]

if __name__ == '__main__':
    sample_data = [False, False, False, True, False]
    status = evaluate_truth_presence(sample_data)
    print(status)