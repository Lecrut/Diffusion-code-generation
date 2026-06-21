import itertools

def sum_second_elements(tuples_list):
    if not all((isinstance(item, tuple) and len(item) == 2 for item in tuples_list)):
        raise ValueError('All elements must be tuples of two elements')
    return sum(itertools.starmap(lambda _, y: y, tuples_list))
if __name__ == '__main__':
    sample_data = [(1, 2), (3, 4), (5, 6), (7, 8)]
    print(sum_second_elements(sample_data))