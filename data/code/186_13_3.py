def reverse_list(lst):
    left, right = (0, len(lst) - 1)
    while left < right:
        lst[left], lst[right] = (lst[right], lst[left])
        left += 1
        right -= 1
if __name__ == '__main__':
    sample_list = ['python', 'is', 'fun']
    reverse_list(sample_list)
    print(sample_list)