def find_middle(numbers):
    if not numbers:
        return None
    n = len(numbers)
    if n % 2 == 1:
        middle_index = n // 2
        return numbers[middle_index]
    else:
        middle_right_index = n // 2
        middle_left_index = middle_right_index - 1
        return (numbers[middle_left_index] + numbers[middle_right_index]) / 2
if __name__ == '__main__':
    sample_sequence = [1, 5, 2, 8, 3]
    if not sample_sequence:
        print("Input sequence is empty.")
    else:
        middle_value = find_middle(sample_sequence)
        print(middle_value)