def average_of_tuples(tuples):
    total_sum = sum(sum(t) for t in tuples)
    total_count = sum(len(t) for t in tuples)
    return total_sum / total_count if total_count > 0 else 0

if __name__ == '__main__':
    sample_data = ((1, 2), (3, 4), (5,))
    print(average_of_tuples(sample_data))