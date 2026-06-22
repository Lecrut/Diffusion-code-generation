def compare_adjacent_elements(lst):
    return [b if a < b else 'equal' if a == b else 'decreasing' for a, b in zip(lst, lst[1:])]

if __name__ == '__main__':
    sample_list = [3, 5, 2, 8, 7, 9]
    print(compare_adjacent_elements(sample_list))