def reverse_list_in_place(lst):
    LEFT = 0
    RIGHT = len(lst) - 1

    while LEFT < RIGHT:
        lst[LEFT], lst[RIGHT] = lst[RIGHT], lst[LEFT]
        LEFT += 1
        RIGHT -= 1

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    reverse_list_in_place(sample_list)
    print(sample_list)