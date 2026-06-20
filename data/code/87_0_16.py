def combine_conditions(numbers, condition_a, condition_b):
    if not all(callable(cond) for cond in [condition_a, condition_b]):
        raise ValueError("Both conditions must be callable functions.")
    
    result = []
    for num in numbers:
        if condition_a(num) and condition_b(num):
            result.append(num)
    return result

if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    condition_a = lambda x: x % 2 == 0
    condition_b = lambda x: x > 5
    combined_list = combine_conditions(data, condition_a, condition_b)
    print(combined_list)