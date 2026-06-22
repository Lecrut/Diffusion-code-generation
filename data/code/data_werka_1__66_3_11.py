def is_adjacent_pairwise_increasing(lst):
    for i in range(len(lst) - 1):
        yield lst[i] < lst[i + 1]

if __name__ == '__main__':
    sample_input = [1, 3, 5, 7, 9]
    result = list(is_adjacent_pairwise_increasing(sample_input))
    print(result)
    
    sample_input_2 = [1, 5, 3, 7]
    result_2 = list(is_adjacent_pairwise_increasing(sample_input_2))
    print(result_2)