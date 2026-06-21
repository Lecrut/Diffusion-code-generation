def get_middle(sequence):
    length = len(sequence)
    index = length // 2
    return sequence[index]

if __name__ == '__main__':
    assert get_middle([1, 2, 3]) == 2
    assert get_middle([1]) == 1
    assert get_middle([1, 2, 3, 4]) == 3
    assert get_middle([1, 2]) == 2
    print(get_middle([1, 2, 3, 4, 5]))
    print(get_middle(['a', 'b', 'c', 'd']))
    print(get_middle([10]))