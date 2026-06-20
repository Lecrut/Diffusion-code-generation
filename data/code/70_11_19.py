def print_first_last(lst):
    if not isinstance(lst, list) or not all(isinstance(item, str) for item in lst):
        raise ValueError("Input must be a list of strings")
    if len(lst) == 0:
        return None, None
    first = lst[0]
    last = lst[-1]
    return first, last

if __name__ == '__main__':
    sample_lists = [
        ['apple', 'banana', 'cherry'],
        ['hello'],
        [],
        ['one', 'two'],
        ['single']
    ]
    
    for i, sample_list in enumerate(sample_lists):
        print(f"Sample List {i+1}: {print_first_last(sample_list)}")