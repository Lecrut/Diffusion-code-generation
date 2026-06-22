def compare_adjacent_elements(lst):
    return ['increasing' if lst[i] < lst[i+1] else 'decreasing' if lst[i] > lst[i+1] else 'equal' for i in range(len(lst)-1)]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 2, 1]
    print(compare_adjacent_elements(sample_list))