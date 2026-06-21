from itertools import starmap

def sum_second_elements(tuples_list):
    return sum(starmap(lambda _, y: y, tuples_list))

if __name__ == '__main__':
    sample_data = [
        (1, 2),
        (3, 4),
        (5, 6)
    ]
    result = sum_second_elements(sample_data)
    print(result)