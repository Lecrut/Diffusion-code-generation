def middle_element(seq):
    assert len(seq) > 0
    mid_index = len(seq) // 2
    return seq[mid_index]

if __name__ == '__main__':
    result = middle_element([1, 2, 3])
    print(result)
    
    result2 = middle_element([1, 2, 3, 4, 5])
    print(result2)
    
    result3 = middle_element([42])
    print(result3)