def middle_element(seq):
    n = len(seq)
    idx = n // 2
    return seq[idx]

if __name__ == '__main__':
    assert middle_element([10, 20, 30, 40, 50]) == 30
    assert middle_element([1, 2]) == 2
    assert middle_element([7]) == 7
    result = middle_element([100, 200, 300, 400])
    print(result)