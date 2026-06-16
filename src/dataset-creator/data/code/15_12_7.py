import timeit
def sort_numerical_data(data):
    return sorted(data)
if __name__ == '__main__':
    sample_list = [5, 23, -10, 45, 78, 9, 6]
    result = sort_numerical_data(sample_list.copy())
    time_taken = timeit.timeit('sort_numerical_data([5, 23, -10])', setup='from __main__ import sort_numerical_data')