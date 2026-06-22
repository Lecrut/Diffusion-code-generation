def is_list_sorted_ascending(numbers):
    def validate_input(numbers):
        if not isinstance(numbers, list):
            raise ValueError("Input must be a list.")
        for num in numbers:
            if not isinstance(num, int):
                raise ValueError("All elements in the list must be integers.")

    def check_adjacent_increasing(numbers):
        return all(numbers[i+1] > numbers[i] for i in range(len(numbers) - 1))

    validate_input(numbers)
    return check_adjacent_increasing(numbers)

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    output = is_list_sorted_ascending(sample_list)
    print(output)