def middle_element(seq):
    return seq[len(seq) // 2]

if __name__ == '__main__':
    assert middle_element([1, 2, 3]) == 2
    assert middle_element([1, 2, 3, 4, 5]) == 3
    assert middle_element([10]) == 10
    print(middle_element([1, 2, 3]))
    print(middle_element([1, 2, 3, 4, 5]))
    print(middle_element([10]))