def is_sorted_ascending(numbers):
    for i in range(1, len(numbers)):
        if numbers[i] < numbers[i - 1]:
            return False
    return True

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(is_sorted_ascending(sample_list))