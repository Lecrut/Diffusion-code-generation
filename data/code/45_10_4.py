def find_minimum(numbers):
    current_min = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] < current_min:
            current_min = numbers[i]
    return current_min

if __name__ == '__main__':
    sample_list = [34, 15, 88, 2, 67, 90, 12]
    result = find_minimum(sample_list)
    print(result)