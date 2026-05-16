def find_middle(numbers):
    if not numbers:
        return None
    n = len(numbers)
    if n % 2 == 1:
        return numbers[n // 2]
    else:
        return (numbers[n // 2 - 1] + numbers[n // 2]) // 2
if __name__ == '__main__':
    sample_input = [1, 5, 2, 8, 3]
    validated_numbers = []
    is_valid = True
    for item in sample_input:
        if isinstance(item, int):
            validated_numbers.append(item)
        else:
            is_valid = False
            break
    if is_valid:
        middle_value = find_middle(validated_numbers)
        print(middle_value)
    else:
        print("Error: Input sequence contains non-integer values.")