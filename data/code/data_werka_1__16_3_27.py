def check_all_positive(numbers):
    return all((num > 0 for num in numbers))
if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5]
    print(check_all_positive(sample_values))
    sample_values = [-1, 2, 3, 4, 5]
    print(check_all_positive(sample_values))
    sample_values = [0, 2, 3, 4, 5]
    print(check_all_positive(sample_values))