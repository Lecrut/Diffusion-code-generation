def group_data_by_bins(data, bins):
    grouped_data = {}
    for item in data:
        found_bin = False
        for upper_bound in bins:
            if item <= upper_bound:
                bin_key = upper_bound
                if bin_key not in grouped_data:
                    grouped_data[bin_key] = []
                grouped_data[bin_key].append(item)
                found_bin = True
        if not found_bin:
            for upper_bound in bins:
                if item > upper_bound:
                    break
            if item > bins[-1]:
                grouped_data[bins[-1]] = grouped_data.get(bins[-1], [])
                grouped_data[bins[-1]].append(item)
    return grouped_data
if __name__ == '__main__':
    sample_data = [1, 5, 2, 8, 3, 9, 4, 7, 6]
    sample_bins = [3, 6, 9]
    result = group_data_by_bins(sample_data, sample_bins)
    print(result)