def get_middle(seq):
    mid_index = len(seq) // 2
    return seq[mid_index]

if __name__ == '__main__':
    result = get_middle([1, 2, 3, 4, 5])
    print(result)
    assert result == 3, "Middle of [1, 2, 3, 4, 5] should be 3"
    
    result2 = get_middle([10, 20])
    print(result2)
    assert result2 == 20, "Middle of [10, 20] should be 20"
    
    result3 = get_middle([42])
    print(result3)
    assert result3 == 42, "Middle of [42] should be 42"