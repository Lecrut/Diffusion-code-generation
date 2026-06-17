def reverse_iterator(iterable):
    return reversed(iterable)
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    sample_tuple = (6, 7, 8)
    print("Reversing list:")
    for item in reverse_iterator(sample_list):
        print(item)
    print("\nReversing tuple:")
    for item in reverse_iterator(sample_tuple):
        print(item)