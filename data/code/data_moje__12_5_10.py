def get_middle_element(sequence):
    assert isinstance(sequence, (list, tuple))
    assert len(sequence) > 0
    middle_index = len(sequence) // 2
    return sequence[middle_index]

if __name__ == '__main__':
    seq1 = [1, 2, 3, 4, 5]
    result1 = get_middle_element(seq1)
    print(result1)
    
    seq2 = [10, 20, 30]
    result2 = get_middle_element(seq2)
    print(result2)
    
    seq3 = [42]
    result3 = get_middle_element(seq3)
    print(result3)
    
    assert result1 == 3
    assert result2 == 20
    assert result3 == 42