def average_pairs(nested_tuples):
    averages = []
    for pair in nested_tuples:
        if len(pair) == 2:
            avg = (pair[0] + pair[1]) / 2
            averages.append(avg)
    return averages

if __name__ == '__main__':
    sample_data = ((1, 2), (3, 4), (5, 6))
    print(average_pairs(sample_data))