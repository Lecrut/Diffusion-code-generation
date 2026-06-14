import sys
def calculate_middle(numbers):
    n = len(numbers)
    if n == 0:
        return None
    if n % 2 == 1:
        middle_index = n // 2
        return numbers[middle_index]
    else:
        middle_right_index = n // 2
        middle_left_index = middle_right_index - 1
        return (numbers[middle_left_index] + numbers[middle_right_index]) / 2.0
if __name__ == '__main__':
    sample_sequence = [1, 5, 9, 13, 17]
    result = calculate_middle(sample_sequence)
    print(result)