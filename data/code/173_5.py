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
        if not found_bin and bins:
            grouped_data["exceeds_all"] = grouped_data.get("exceeds_all", []) + [item]
    return grouped_data
if __name__ == '__main__':
    sample_data = [10, 5, 22, 3, 15, 8, 25, 1, 12]
    sample_bins = [10, 20, 30]
    result = group_data_by_bins(sample_data, sample_bins)
    print(result)