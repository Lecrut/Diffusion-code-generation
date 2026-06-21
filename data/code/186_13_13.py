def reverse_list_in_place(lst):
    left, right = 0, len(lst) - 1
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    reverse_list_in_place(sample_list)
    print(sample_list)