def find_median(lst):
    if not lst:
        return None
    n = len(lst)
    if n % 2 == 1:
        return lst[n // 2]
    else:
        mid1 = lst[n // 2 - 1]
        mid2 = lst[n // 2]
        return (mid1 + mid2) / 2.0

def calculate_median_of_lists(data):
    medians = []
    for sample in data:
        sorted_sample = sorted(sample)
        median = find_median(sorted_sample)
        medians.append(median)
    return medians

if __name__ == '__main__':
    sample_data = [
        [1, 3, 5],
        [2, 4, 6, 8],
        [],
        [7]
    ]
    print(calculate_median_of_lists(sample_data))