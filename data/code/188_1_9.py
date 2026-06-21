def reverse_in_place(lst):
    left = 0
    right = len(lst) - 1
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1

if __name__ == '__main__':
    sample_list = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    reverse_in_place(sample_list)
    print(sample_list)