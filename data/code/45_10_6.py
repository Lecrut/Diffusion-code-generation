def find_minimum(numbers):
    current_min = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] < current_min:
            current_min = numbers[i]
    return current_min

if __name__ == '__main__':
    sample_list = [34, -50, 42, 14, -99, 100]
    result = find_minimum(sample_list)
    print(result)