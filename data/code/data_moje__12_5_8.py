def get_middle(sequence):
    length = len(sequence)
    index = length // 2
    return sequence[index]

if __name__ == '__main__':
    assert get_middle([1, 2, 3]) == 2
    assert get_middle([10, 20, 30, 40, 50]) == 30
    assert get_middle([100, 200, 300, 400]) == 300
    
    sample_list = [4, 8, 15, 16, 23, 42]
    result = get_middle(sample_list)
    print(result)