def get_first_last_string(strings):
    if not strings:
        return None, None
    first = strings[0]
    last = strings[-1]
    return first, last

if __name__ == '__main__':
    sample_lists = [
        ['hello', 'world'],
        ['single'],
        [],
        ['first', 'second', 'third', 'fourth']
    ]
    
    for lst in sample_lists:
        print(f"List: {lst} -> First and Last: {get_first_last_string(lst)}")