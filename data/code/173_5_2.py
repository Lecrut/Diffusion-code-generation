def group_data(data, bins):
    grouped = {}
    for item in data:
        found_bin = None
        for i, upper_bound in enumerate(bins):
            if item <= upper_bound:
                if upper_bound not in grouped:
                    grouped[upper_bound] = []
                grouped[upper_bound].append(item)
                break
        if found_bin is None:
            pass
    return grouped
if __name__ == '__main__':
    sample_data = [10, 5, 22, 15, 3, 25, 8, 12]
    sample_bins = [10, 20, 30]
    result = group_data(sample_data, sample_bins)
    print(result)