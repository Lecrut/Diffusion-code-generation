def compare_adjacent_numbers(data):
    if len(data) < 2:
        return True
    for i in range(len(data) - 1):
        if not (isinstance(data[i], (int, float)) and isinstance(data[i + 1], (int, float))):
            raise TypeError(f'Non-numeric adjacent elements found: {data[i]} and {data[i + 1]}')
        if data[i] > data[i + 1]:
            return False
    return True
if __name__ == '__main__':
    sample_list_1 = [1, 2, 3, 4, 5]
    sample_list_2 = [1, 'a', 3, 4, 5]
    sample_list_3 = [5.0, 4.5, 4.0, 3.5, 3.0]
    sample_list_4 = [1, 1, 2, 2, 3]
    sample_list_5 = []
    try:
        print(compare_adjacent_numbers(sample_list_1))
    except TypeError as e:
        print(e)
    try:
        print(compare_adjacent_numbers(sample_list_2))
    except TypeError as e:
        print(e)
    try:
        print(compare_adjacent_numbers(sample_list_3))
    except TypeError as e:
        print(e)
    try:
        print(compare_adjacent_numbers(sample_list_4))
    except TypeError as e:
        print(e)
    try:
        print(compare_adjacent_numbers(sample_list_5))
    except TypeError as e:
        print(e)