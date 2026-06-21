def reverse_list(lst):
    if not isinstance(lst, list):
        raise ValueError("Input must be a list.")
    lst.reverse()
    return lst

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print('Original list:', sample_list)
    try:
        reversed_sample = reverse_list(sample_list)
        print('Reversed list:', reversed_sample)
    except ValueError as e:
        print(e)