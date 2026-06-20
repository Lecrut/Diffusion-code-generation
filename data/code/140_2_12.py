def is_sorted_ascending(numbers):
    return all(numbers[i] <= numbers[i + 1] for i in range(len(numbers) - 1))

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(is_sorted_ascending(sample_list))