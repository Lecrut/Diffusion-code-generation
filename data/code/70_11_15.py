def print_first_last(strings):
    if not strings:
        return None, None
    first = strings[0]
    last = strings[-1]
    return first, last

if __name__ == '__main__':
    sample_list1 = ['apple', 'banana', 'cherry']
    sample_list2 = ['red', 'green', 'blue', 'yellow']
    sample_list3 = []
    
    print(f"List 1: {print_first_last(sample_list1)}")
    print(f"List 2: {print_first_last(sample_list2)}")
    print(f"List 3: {print_first_last(sample_list3)}")