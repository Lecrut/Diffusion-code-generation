def validate_input(lst):
    if not isinstance(lst, list) or not all(isinstance(item, (int, float, str)) for item in lst):
        raise ValueError("Input must be a list of integers, floats, or strings")

def reverse_list_in_place(lst):
    left, right = 0, len(lst) - 1
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    validate_input(sample_list)
    reverse_list_in_place(sample_list)
    print(sample_list)