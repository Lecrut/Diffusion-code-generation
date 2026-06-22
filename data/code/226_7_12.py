def duplicate_list(input_list):
    if not isinstance(input_list, list) or not all(isinstance(x, bool) for x in input_list):
        raise ValueError("Input must be a list of boolean values")
    
    result = input_list[:]
    for _ in range(9):
        result += input_list
    
    return result

if __name__ == '__main__':
    sample_list = [True, False] * 5
    final_list = duplicate_list(sample_list)
    print(final_list)