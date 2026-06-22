def get_center_element(sequence):
    n = len(sequence)
    if n == 0:
        return None
    return sequence[n // 2]

if __name__ == '__main__':
    print(get_center_element([1, 2, 3, 4, 5]))
    print(get_center_element((10, 20, 30)))
    print(get_center_element([42]))
    print(get_center_element([]))
    print(get_center_element([1, 2]))