def print_first_last(strings):
    if not strings:
        return
    first = strings[0]
    last = strings[-1]
    print(first)
    print(last)

if __name__ == '__main__':
    sample_lists = [
        ['apple', 'banana', 'cherry'],
        ['hello'],
        [],
        ['a', 'b', 'c', 'd', 'e'],
        ['single']
    ]
    for lst in sample_lists:
        print_first_last(lst)