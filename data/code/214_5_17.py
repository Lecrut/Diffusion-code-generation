def smallest_positive_number(numbers):
    return min([num for num in numbers if num > 0])

if __name__ == '__main__':
    sample_numbers = [-5, -2, 3, 1, 4]
    print(smallest_positive_number(sample_numbers))