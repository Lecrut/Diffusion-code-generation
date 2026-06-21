from itertools import starmap

def sum_second_elements(tuples_list):
    if not all(isinstance(item, tuple) and len(item) >= 2 for item in tuples_list):
        raise ValueError("All items in the list must be tuples with at least two elements.")
    
    return sum(starmap(lambda x, y: y, tuples_list))

if __name__ == '__main__':
    sample_data = [
        (1, 2),
        (3, 4),
        (5, 6)
    ]
    print(sum_second_elements(sample_data))