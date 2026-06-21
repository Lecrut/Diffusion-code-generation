def reverse_list_in_place(lst):
    left = 0
    right = len(lst) - 1
    while left < right:
        lst[left], lst[right] = (lst[right], lst[left])
        left += 1
        right -= 1

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    reverse_list_in_place(sample_values)
    print(sample_values)