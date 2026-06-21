def find_largest_value(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

if __name__ == '__main__':
    sample_values1 = (3.14, 2.71, 1.618, 0.577)
    print(find_largest_value(sample_values1))
    sample_values2 = (10, 5, 20, 8)
    print(find_largest_value(sample_values2))
    sample_values3 = (-5, -1, -10, -3)
    print(find_largest_value(sample_values3))
    sample_values4 = [42]
    print(find_largest_value(sample_values4))