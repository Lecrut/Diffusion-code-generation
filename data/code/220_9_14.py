def average_of_tuples(tuples):
    if not tuples:
        return 0
    total = sum(sum(t) for t in tuples)
    count = sum(len(t) for t in tuples)
    return total / count

if __name__ == '__main__':
    sample_values = ((1, 2), (3, 4), (5,))
    print(average_of_tuples(sample_values))