def group_data(data, bins):
    grouped = {}
    for item in data:
        found_bin = False
        for upper_bound in bins:
            if item <= upper_bound:
                pass
        for upper_bound in sorted(bins):
            if item <= upper_bound:
                bin_key = upper_bound
                grouped[bin_key] = grouped.get(bin_key, []) + [item]
                break
    return grouped
if __name__ == '__main__':
    sample_data = [10, 25, 3, 40, 15, 5, 30, 8]
    sample_bins = [10, 20, 30, 40]
    result = group_data(sample_data, sample_bins)
    print(result)