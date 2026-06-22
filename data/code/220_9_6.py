def average_of_tuples(tuples):
    total = sum(sum(t) for t in tuples)
    count = len(tuples) * len(tuples[0])
    return total / count

if __name__ == '__main__':
    sample_data = ((1, 2), (3, 4), (5, 6))
    print(average_of_tuples(sample_data))