def get_middle_element(seq):
    if not seq:
        raise ValueError("Sequence is empty")
    mid_index = len(seq) // 2
    return seq[mid_index]

if __name__ == '__main__':
    sample1 = [1, 2, 3, 4, 5]
    sample2 = [10, 20, 30, 40]
    sample3 = ['a', 'b', 'c']
    sample4 = [42]
    
    assert get_middle_element(sample1) == 3
    assert get_middle_element(sample2) == 30
    assert get_middle_element(sample3) == 'b'
    assert get_middle_element(sample4) == 42
    
    print(get_middle_element(sample1))
    print(get_middle_element(sample2))
    print(get_middle_element(sample3))
    print(get_middle_element(sample4))