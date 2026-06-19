def adjacent_pairs_generator(lst):
    for i in range(len(lst) - 1):
        yield lst[i] < lst[i + 1]

if __name__ == '__main__':
    sample_list = [1, 3, 2, 4, 5]
    for result in adjacent_pairs_generator(sample_list):
        print(result)