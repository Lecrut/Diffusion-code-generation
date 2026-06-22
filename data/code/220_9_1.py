def average_of_tuples(tuples):
    return sum(sum(t) for t in tuples) / len(tuples)

if __name__ == '__main__':
    sample_data = ((1, 2), (3, 4), (5, 6))
    print(average_of_tuples(sample_data))