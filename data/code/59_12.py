def find_middle(numbers):
    n = len(numbers)
    if n == 0:
        return None
    elif n % 2 == 1:
        return numbers[n // 2]
    else:
        return (numbers[n // 2 - 1] + numbers[n // 2]) // 2
if __name__ == '__main__':
    sample_input = [1, 5, 9, 13, 17]
    if not isinstance(sample_input, list) or not all(isinstance(x, int) for x in sample_input):
        print("Error: Sample input is not a list of integers.")
    else:
        middle_item = find_middle(sample_input)
        print(middle_item)