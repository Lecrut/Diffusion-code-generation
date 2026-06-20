def print_first_last(strings):
    first = strings[0] if strings else None
    last = strings[-1] if strings else None
    return first, last

if __name__ == '__main__':
    sample_list1 = ['apple', 'banana', 'cherry']
    sample_list2 = []
    print(f"List 1: {print_first_last(sample_list1)}")
    print(f"List 2: {print_first_last(sample_list2)}")