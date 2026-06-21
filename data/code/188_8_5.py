def reverse_with_swap(lst):
    LEFT = 0
    RIGHT = len(lst) - 1
    while LEFT < RIGHT:
        lst[LEFT], lst[RIGHT] = lst[RIGHT], lst[LEFT]
        LEFT += 1
        RIGHT -= 1

if __name__ == '__main__':
    sample_list = [5, 4, 3, 2, 1]
    reverse_with_swap(sample_list)
    print(sample_list)