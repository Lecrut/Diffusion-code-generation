def count_first_elements(tuples):
    counts = {}
    for t in tuples:
        if len(t) > 0:
            first_element = t[0]
            if first_element in counts:
                counts[first_element] += 1
            else:
                counts[first_element] = 1
    return counts

def validate_input(tuples):
    for t in tuples:
        if not isinstance(t, tuple) or len(t) == 0:
            raise ValueError("Input must be a non-empty tuple of tuples.")

if __name__ == '__main__':
    sample_tuples = ((1, 'a'), (2, 'b'), (1, 'c'), (3, 'd'), (2, 'e'))
    validate_input(sample_tuples)
    result = count_first_elements(sample_tuples)
    print(result)