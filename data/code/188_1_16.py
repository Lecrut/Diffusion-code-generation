START_INDEX = 0
END_INDEX = -1

def reverse_in_place(lst):
    left = START_INDEX
    right = len(lst) + END_INDEX
    while left < right:
        lst[left], lst[right] = (lst[right], lst[left])
        left += 1
        right -= 1
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    reverse_in_place(sample_list)
    print(sample_list)