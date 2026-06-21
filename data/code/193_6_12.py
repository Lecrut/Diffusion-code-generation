def sum_mixed_numbers(numbers):
    total = 0
    for number in numbers:
        if isinstance(number, int) or isinstance(number, float):
            total += number
        else:
            raise TypeError("All elements must be either int or float")
    return total

if __name__ == '__main__':
    sample_values = [1, 2.5, 3, 4.75]
    print(sum_mixed_numbers(sample_values))