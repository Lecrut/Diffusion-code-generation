def find_middle_item(numbers):
    if not numbers:
        return None
    middle_index = len(numbers) // 2
    return numbers[middle_index]
if __name__ == '__main__':
    sample_sequence_odd = [1, 3, 5, 7, 9]
    sample_sequence_even = [2, 4, 6, 8, 10, 12]
    print(find_middle_item(sample_sequence_odd))
    print(find_middle_item(sample_sequence_even))