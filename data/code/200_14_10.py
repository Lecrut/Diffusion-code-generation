import itertools

def sum_second_elements(tuples_list):
    if not all(isinstance(t, tuple) and len(t) >= 2 for t in tuples_list):
        raise ValueError("All elements must be tuples with at least two items")
    
    return sum(itertools.starmap(lambda _, b: b, tuples_list))

if __name__ == '__main__':
    sample_data = [
        (1, 2),
        (3, 4),
        (5, 6)
    ]
    print(sum_second_elements(sample_data))