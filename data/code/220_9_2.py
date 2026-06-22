def average_of_tuples(tuples):
    total = sum(sum(t) for t in tuples)
    count = sum(len(t) for t in tuples)
    return total / count if count > 0 else 0

if __name__ == '__main__':
    sample_data = ((1, 2), (3, 4), (5,))
    print(average_of_tuples(sample_data))