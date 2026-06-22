def find_minimum(numbers):
    if not numbers:
        raise ValueError("The list is empty")
    return min(numbers)

if __name__ == '__main__':
    sample_list = [3.5, 1.2, 7.8, -2.3, 4.6]
    result = find_minimum(sample_list)
    print(result)