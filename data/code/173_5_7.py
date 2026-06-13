def group_data(data, bins):
    grouped = {}
    for item in data:
        found = False
        for upper_bound in bins:
            if item <= upper_bound:
                bin_key = upper_bound
                if bin_key not in grouped:
                    grouped[bin_key] = []
                grouped[bin_key].append(item)
                found = True
        if not found:
            for upper_bound in bins:
                if item > upper_bound:
                    break
                pass
    return grouped
if __name__ == '__main__':
    sample_data = [10, 25, 3, 40, 15, 5, 30, 8]
    sample_bins = [10, 20, 30]
    result = group_data(sample_data, sample_bins)
    print(result)