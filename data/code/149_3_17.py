def reverse_list(lst):
    left = 0
    right = len(lst) - 1
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1
    return lst

if __name__ == '__main__':
    sample_list = [3, 5, 7, 9, 11]
    reversed_list = reverse_list(sample_list)
    print(reversed_list)