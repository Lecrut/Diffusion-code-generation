def reverse_with_swap(lst):
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