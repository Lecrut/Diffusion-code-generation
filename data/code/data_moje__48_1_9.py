def find_largest_integer(numbers):
    max_value = numbers[0]
    [max_value := n if n > max_value else max_value for n in numbers[1:]]
    return max_value

if __name__ == '__main__':
    sample_numbers = [3, 5, 1, 9, -2, 15, 7, 4, 8, 2]
    result = find_largest_integer(sample_numbers)
    print(result)