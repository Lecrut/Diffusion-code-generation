def get_middle_element(sequence):
    return sequence[len(sequence) // 2]

if __name__ == '__main__':
    assert get_middle_element([1, 2, 3]) == 2
    assert get_middle_element([1, 2, 3, 4, 5]) == 3
    assert get_middle_element([10, 20, 30, 40]) == 20
    print(get_middle_element([5, 10, 15, 20, 25]))
    print(get_middle_element([1, 2, 3, 4, 5, 6]))