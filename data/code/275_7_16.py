def is_even(number):
    return number % 2 == 0

def filter_even_tuples(tuples_list):
    if not all(isinstance(t, tuple) and len(t) > 1 for t in tuples_list):
        raise ValueError("All elements must be tuples with at least two items")
    
    return [t for t in tuples_list if is_even(t[1])]

if __name__ == '__main__':
    sample_data = [(1, 2), (3, 4), (5, 6), (7, 8)]
    result = filter_even_tuples(sample_data)
    print(result)