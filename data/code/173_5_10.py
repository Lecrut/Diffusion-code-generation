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
                if bins and item > bins[-1]:
                    grouped[bins[-1]] = grouped.get(bins[-1], [])
                    grouped[bins[-1]].append(item)
                    break
    return grouped
if __name__ == '__main__':
    sample_data = [1, 5, 12, 3, 8, 15, 2, 9]
    sample_bins = [5, 10, 15]
    result = group_data(sample_data, sample_bins)
    print(result)