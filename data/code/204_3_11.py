def find_middle(numbers):
    if not numbers:
        raise ValueError("Input tuple is empty.")
    n = len(numbers)
    if n != 5:
        raise ValueError("Input tuple must contain exactly five elements.")
    middle_index = n // 2
    return numbers[middle_index]

if __name__ == '__main__':
    sample_input = (10.5, 20.3, 30.7, 40.2, 50.8)
    try:
        middle_value = find_middle(sample_input)
        print(middle_value)
    except ValueError as e:
        print(e)