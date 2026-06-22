def reverse_dict_keys(d):
    return {k: d[k] for k in reversed(list(d.keys()))}

if __name__ == '__main__':
    my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    print("Original dictionary:", my_dict)
    reversed_dict = reverse_dict_keys(my_dict)
    print("Reversed keys dictionary:", reversed_dict)
    my_dict_2 = {'z': 26, 'y': 25, 'x': 24, 'w': 23}
    print("Original dictionary:", my_dict_2)
    reversed_dict_2 = reverse_dict_keys(my_dict_2)
    print("Reversed keys dictionary:", reversed_dict_2)