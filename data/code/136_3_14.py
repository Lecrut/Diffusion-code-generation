def filter_tuples(tuples, min_age=18, max_income=None):
    if not all(isinstance(t, tuple) and len(t) == 3 for t in tuples):
        raise ValueError("All elements must be 3-element tuples")

    def is_valid_tuple(t):
        age, income, _ = t
        return min_age <= age <= (max_income if max_income is not None else float('inf'))

    return list(filter(is_valid_tuple, tuples))

if __name__ == '__main__':
    sample_tuples = [
        (25, 50000, 'Developer'),
        (30, 75000, 'Manager'),
        (17, 40000, 'Student'),
        (35, None, 'Consultant')
    ]
    
    filtered_tuples = filter_tuples(sample_tuples)
    print(filtered_tuples)