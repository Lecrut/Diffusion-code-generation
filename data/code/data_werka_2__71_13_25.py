def get_middle_element(items):
    count = len(items)
    if count == 0:
        raise ValueError("List must not be empty")
    half = count // 2
    if count % 2 == 1:
        return items[half]
    return items[half - 1]

if __name__ == '__main__':
    print(get_middle_element([1, 2, 3]))
    print(get_middle_element([1, 2, 3, 4]))
    print(get_middle_element([7]))
    print(get_middle_element([5, 10]))
    print(get_middle_element([1, 2, 3, 4, 5, 6, 7, 8]))
    print(get_middle_element([10, 20, 30, 40, 50]))