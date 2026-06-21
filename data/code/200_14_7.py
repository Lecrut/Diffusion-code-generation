import itertools

def sum_second_elements(tuples_list):
    return sum(itertools.starmap(lambda _, y: y, tuples_list))

if __name__ == '__main__':
    sample_tuples = [(1, 2), (3, 4), (5, 6)]
    print(sum_second_elements(sample_tuples))