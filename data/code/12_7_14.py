def get_middle(sequence):
    if not isinstance(sequence, (list, tuple, str)):
        raise TypeError("Sequence type expected")
    
    length = len(sequence)
    
    if length == 0:
        return None
    
    if length % 2 == 1:
        mid_index = length // 2
        return sequence[mid_index]
    else:
        mid_index = length // 2
        return sequence[mid_index - 1]

if __name__ == '__main__':
    print(get_middle([1, 2, 3, 4, 5]))
    print(get_middle([1, 2, 3, 4]))
    print(get_middle((10, 20, 30)))
    print(get_middle("python"))
    print(get_middle([42]))
    print(get_middle([]))