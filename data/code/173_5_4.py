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
            pass
    return grouped_data
if __name__ == '__main__':
    sample_data = [12, 5, 23, 8, 15, 30, 7]
    sample_bins = [10, 20, 30]
    result = group_data_by_bins(sample_data, sample_bins)
    print(result)