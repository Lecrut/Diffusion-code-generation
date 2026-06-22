def is_non_decreasing(numbers):
    def validate_input(numbers):
        if not all(isinstance(x, int) for x in numbers):
            raise ValueError("All elements must be integers")
        if len(numbers) < 2:
            return True

    try:
        validate_input(numbers)
        return all(numbers[i] <= numbers[i + 1] for i in range(len(numbers) - 1))
    except ValueError as e:
        print(e)
        return False

if __name__ == '__main__':
    sample_input_1 = [1, 3, 5, 7]
    sample_input_2 = [1, 5, 3, 7]
    sample_input_3 = [10, 20, 20, 30]
    sample_input_4 = [5, 5, 5]
    sample_input_5 = [1, 2, 1]

    print(is_non_decreasing(sample_input_1))
    print(is_non_decreasing(sample_input_2))
    print(is_non_decreasing(sample_input_3))
    print(is_non_decreasing(sample_input_4))
    print(is_non_decreasing(sample_input_5))