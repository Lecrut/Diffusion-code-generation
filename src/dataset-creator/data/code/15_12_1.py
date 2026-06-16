import timeit
def sort_numeric_data(data):
    return sorted(data)
if __name__ == '__main__':
    sample_data = [64, 34, 25, 12, 22, 11, 90]
    result = sort_numeric_data(sample_data.copy())
    print(result)