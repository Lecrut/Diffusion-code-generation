def get_element(sequence, index):
    if not isinstance(sequence, (list, tuple)):
        raise TypeError("The sequence must be a list or tuple.")
    if not isinstance(index, int):
        raise TypeError("The index must be an integer.")
    if index < 0 or index >= len(sequence):
        raise IndexError("Index out of range.")
    
    return sequence[index]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    sample_tuple = ('a', 'b', 'c', 'd', 'e')
    print(get_element(sample_list, 2))
    print(get_element(sample_tuple, 3))