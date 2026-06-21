def create_lookup_table(list1, list2):
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise ValueError("Both arguments must be lists.")
    if len(list1) != len(list2):
        raise ValueError("Lists must have the same length.")
    
    return dict(zip(list1, list2))

if __name__ == '__main__':
    keys = ['apple', 'banana', 'carrot']
    values = ['fruit', 'fruit', 'vegetable']
    lookup_table = create_lookup_table(keys, values)
    print(lookup_table)