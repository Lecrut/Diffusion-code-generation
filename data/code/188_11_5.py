def validate_input(input_list):
    if not isinstance(input_list, list):
        raise ValueError("Input must be a list.")

def reverse_list_in_place(lst):
    validate_input(lst)
    lst.reverse()

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print('Original list:', sample_list)
    reverse_list_in_place(sample_list)
    print('Reversed list:', sample_list)