def reverse_with_swap(lst):
    if not isinstance(lst, list) or not all((isinstance(x, (int, float)) for x in lst)):
        raise ValueError('Input must be a list of numbers')
    left = 0
    right = len(lst) - 1
    while left < right:
        lst[left], lst[right] = (lst[right], lst[left])
        left += 1
        right -= 1
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    reverse_with_swap(sample_list)
    print(sample_list)
    sample_list = [10, 20, 30, 40, 50, 60]
    reverse_with_swap(sample_list)
    print(sample_list)
    sample_list = [7.5, 8.5, 9.5, 10.5, 11.5, 12.5]
    reverse_with_swap(sample_list)
    print(sample_list)