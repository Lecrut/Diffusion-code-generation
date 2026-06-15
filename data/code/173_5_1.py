def group_data_by_bins(data, bins):
    grouped_data = {}
    for item in data:
        found_bin = False
        for bin_upper in bins:
            if item <= bin_upper:
                bin_key = bin_upper
                if bin_key not in grouped_data:
                    grouped_data[bin_key] = []
                grouped_data[bin_key].append(item)
                found_bin = True
                break
        if not found_bin:
            if 'overflow' not in grouped_data:
                grouped_data['overflow'] = []
            grouped_data['overflow'].append(item)
    return grouped_data
if __name__ == '__main__':
    sample_data = [10, 25, 32, 5, 40, 15, 8, 35]
    sample_bins = [20, 30, 45]
    result = group_data_by_bins(sample_data, sample_bins)
    print(result)