def is_sorted_ascending(numbers):
    if not isinstance(numbers, list) or not all(isinstance(n, int) for n in numbers):
        raise ValueError("Input must be a list of integers.")
    
    return all(numbers[i+1] > numbers[i] for i in range(len(numbers) - 1))

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    try:
        output = is_sorted_ascending(sample_list)
        print(output)
    except ValueError as e:
        print(e)