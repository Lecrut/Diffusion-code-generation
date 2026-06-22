def check_ends(sequence):
    if not hasattr(sequence, '__len__'):
        raise ValueError("Input must be a sequence with length")
    length = len(sequence)
    if length == 0:
        return None
    if length == 1:
        return (sequence[0], sequence[0])
    return (sequence[0], sequence[-1])

if __name__ == '__main__':
    print(check_ends([1, 2, 3, 4, 5]))
    print(check_ends("hello"))
    print(check_ends((10,)))
    print(check_ends([]))
    print(check_ends([42]))