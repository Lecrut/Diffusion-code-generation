def adjacent_pairs_generator(lst):
    for i in range(len(lst) - 1):
        yield lst[i] < lst[i + 1]

if __name__ == '__main__':
    sample_list_1 = [1, 3, 5, 7, 9]
    sample_list_2 = [1, 3, 2, 5]
    
    print(list(adjacent_pairs_generator(sample_list_1)))
    print(list(adjacent_pairs_generator(sample_list_2)))