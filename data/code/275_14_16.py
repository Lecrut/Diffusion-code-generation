def count_first_elements(tuples):
    counts = {}
    for t in tuples:
        if len(t) > 0:
            key = t[0]
            counts[key] = counts.get(key, 0) + 1
    return counts

if __name__ == '__main__':
    sample_tuples = ((1, 'a'), (2, 'b'), (1, 'c'), (3, 'd'), (2, 'e'))
    print(count_first_elements(sample_tuples))