def validate_tuples(tuples):
    if not all(isinstance(t, tuple) and len(t) > 0 for t in tuples):
        raise ValueError("All elements must be non-empty tuples.")

def sum_of_elements(tuples):
    return sum(sum(t) for t in tuples)

def count_elements(tuples):
    return sum(len(t) for t in tuples)

def average_of_tuples(tuples):
    validate_tuples(tuples)
    total = sum_of_elements(tuples)
    count = count_elements(tuples)
    return total / count if count > 0 else 0

if __name__ == '__main__':
    sample_data = ((1, 2), (3, 4), (5,))
    print(average_of_tuples(sample_data))