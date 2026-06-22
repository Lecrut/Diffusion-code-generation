def get_middle(sequence):
    if not sequence:
        return None
    index = len(sequence) // 2
    return sequence[index]

if __name__ == '__main__':
    assert get_middle([1, 2, 3]) == 2
    assert get_middle([1, 2, 3, 4]) == 2
    assert get_middle([1]) == 1
    assert get_middle([]) is None
    
    sample_list = [10, 20, 30, 40, 50]
    result = get_middle(sample_list)
    print(result)