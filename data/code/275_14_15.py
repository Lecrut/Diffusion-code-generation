def count_first_elements(tuples):
    counts = {}
    for t in tuples:
        first_element = t[0]
        if first_element in counts:
            counts[first_element] += 1
        else:
            counts[first_element] = 1
    return counts

if __name__ == '__main__':
    sample_tuples = ((4, 'x'), (5, 'y'), (4, 'z'), (6, 'w'), (5, 'v'))
    result = count_first_elements(sample_tuples)
    print(result)