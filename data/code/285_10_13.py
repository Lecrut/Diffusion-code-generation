def max_adjacent_elements(lst):
    return [max(a, b) for a, b in zip(lst[:-1], lst[1:])]

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2]
    print(max_adjacent_elements(sample_list))