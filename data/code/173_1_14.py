from itertools import groupby

def aggregate_tuples(tuples):
    sorted_tuples = sorted(tuples)
    aggregated_result = [(key, sum((value for _, value in group))) for key, group in groupby(sorted_tuples, key=lambda x: x[0])]
    return aggregated_result
if __name__ == '__main__':
    sample_data = [(1, 2), (3, 4), (1, 5), (3, 6), (2, 3)]
    result = aggregate_tuples(sample_data)
    print(result)