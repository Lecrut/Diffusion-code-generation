def check_same_truth_value(bool1: bool, bool2: bool) -> bool:
    return bool1 == bool2

if __name__ == '__main__':
    sample_input1 = True
    sample_input2 = False
    result = check_same_truth_value(sample_input1, sample_input2)
    print(f"Sample Input 1: {sample_input1}, Sample Input 2: {sample_input2}, Result: {result}")