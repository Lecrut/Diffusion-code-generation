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
    sample_tuples = ((1, 'a'), (2, 'b'), (1, 'c'), (3, 'd'), (2, 'e'))
    print(count_first_elements(sample_tuples))