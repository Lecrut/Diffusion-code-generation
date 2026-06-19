def is_sorted_ascending(numbers):
    for i in range(len(numbers) - 1):
        if numbers[i + 1] <= numbers[i]:
            return False
    return True

if __name__ == '__main__':
    sample_list = [3, 5, 8, 9, 10]
    output = is_sorted_ascending(sample_list)
    print(output)