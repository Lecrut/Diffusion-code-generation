def find_middle_item(numbers):
    if not numbers:
        return None
    middle_index = len(numbers) // 2
    return numbers[middle_index]
if __name__ == '__main__':
    sample_values = [1, 3, 5, 7, 9]
    even_sample_values = [2, 4, 6, 8, 10, 12]
    print('Middle item of odd length list:', find_middle_item(sample_values))
    print('Middle item of even length list:', find_middle_item(even_sample_values))