def max_adjacent_elements(lst):
    return [max(lst[i], lst[i+1]) for i in range(len(lst)-1)]

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 6]
    print(max_adjacent_elements(sample_list))