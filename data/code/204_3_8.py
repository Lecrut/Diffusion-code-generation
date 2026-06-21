def find_middle(numbers):
    n = len(numbers)
    if n % 2 == 0:
        raise ValueError("Input tuple must contain an odd number of elements.")
    middle_index = n // 2
    return numbers[middle_index]

if __name__ == '__main__':
    sample_tuple = (10.5, 20.3, 30.7, 40.1, 50.9)
    try:
        middle_value = find_middle(sample_tuple)
        print(middle_value)
    except ValueError as e:
        print(e)