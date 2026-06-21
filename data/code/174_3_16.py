def invert_dictionary(d):
    return {v: k for k, v in d.items()}

if __name__ == '__main__':
    sample_dict = {'x': 1, 'y': 2, 'z': 3}
    inverted_dict = invert_dictionary(sample_dict)
    print(inverted_dict)

    another_dict = {'apple': 'red', 'banana': 'yellow', 'grape': 'purple'}
    inverted_another_dict = invert_dictionary(another_dict)
    print(inverted_another_dict)