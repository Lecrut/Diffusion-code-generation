def check_ends(sequence):
    if not hasattr(sequence, '__getitem__') or not hasattr(sequence, '__len__'):
        raise ValueError("Input must be a sequence type")
    
    length = len(sequence)
    
    if length == 0:
        return None
    
    if length == 1:
        return (sequence[0], sequence[0])
    
    first = sequence[0]
    last = sequence[-1]
    
    return (first, last)

if __name__ == '__main__':
    print(check_ends([1, 2, 3, 4, 5]))
    print(check_ends("hello"))
    print(check_ends((10, 20)))
    print(check_ends([42]))
    print(check_ends([]))