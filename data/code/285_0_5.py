def compare_adjacent_elements(lst):
    return ['increasing' if lst[i] < lst[i+1] else 'decreasing' if lst[i] > lst[i+1] else 'equal' for i in range(len(lst)-1)]

if __name__ == '__main__':
    sample_list = [3, 5, 2, 8, 6, 7]
    print(compare_adjacent_elements(sample_list))