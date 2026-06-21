def validate_input(lst):
    if not all(isinstance(item, int) for item in lst):
        raise ValueError("Error: Invalid input. Please ensure all inputs are integers.")

def reverse_list(lst):
    left = 0
    right = len(lst) - 1
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1
    return lst

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    validate_input(sample_list)
    reversed_list = reverse_list(sample_list)
    print(reversed_list)