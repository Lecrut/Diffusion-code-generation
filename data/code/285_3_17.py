def check_ascending(numbers):
    return [numbers[i] < numbers[i+1] for i in range(len(numbers) - 1)]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(check_ascending(sample_list))
    another_list = [5, 4, 3, 2, 1]
    print(check_ascending(another_list))
    mixed_list = [1, 3, 2, 4, 5]
    print(check_ascending(mixed_list))