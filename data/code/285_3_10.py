def check_ascending_pairs(numbers):
    if not all(isinstance(n, int) for n in numbers):
        raise ValueError("All elements in the list must be integers")
    
    return [numbers[i] < numbers[i+1] for i in range(len(numbers) - 1)]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    results = check_ascending_pairs(sample_list)
    print(results)

    invalid_list = [10, "20", 30, 40]
    try:
        results = check_ascending_pairs(invalid_list)
    except ValueError as e:
        print(e)