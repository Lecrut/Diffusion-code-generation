import itertools

def sum_second_elements(tuples_list):
    return sum(itertools.starmap(lambda _, y: y, tuples_list))

if __name__ == '__main__':
    sample_data = [
        (1, 10),
        (2, 20),
        (3, 30)
    ]
    result = sum_second_elements(sample_data)
    print(result)