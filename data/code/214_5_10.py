def find_smallest_positive(numbers):
    return min([num for num in numbers if num > 0])

if __name__ == '__main__':
    sample_numbers = [-5, -2, 3, 1, 4]
    print(find_smallest_positive(sample_numbers))