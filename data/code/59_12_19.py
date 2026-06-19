MIDDLE_INDEX = "middle_index"
EVEN_LENGTH = "even_length"

def find_middle_item(numbers):
    if not numbers:
        return None
    
    n = len(numbers)
    if n % 2 == 1:
        return numbers[n // 2]
    else:
        middle_right_index = n // 2
        middle_left_index = middle_right_index - 1
        return (numbers[middle_left_index] + numbers[middle_right_index]) // 2

if __name__ == '__main__':
    sample_values = [3, 7, 5, 9, 11]
    result = find_middle_item(sample_values)
    print(result)