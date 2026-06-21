def validate_input(lst):
    if not isinstance(lst, list) or not all(isinstance(item, int) for item in lst):
        raise ValueError("Input must be a list of integers")

def reverse_list_in_place(lst):
    validate_input(lst)
    left = 0
    right = len(lst) - 1
    while left < right:
        lst[left], lst[right] = (lst[right], lst[left])
        left += 1
        right -= 1

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    reverse_list_in_place(sample_list)
    print(sample_list)