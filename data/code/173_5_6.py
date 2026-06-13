def group_data(data, bins):
    grouped = {}
    for item in data:
        found_bin = None
        for i, upper_bound in enumerate(bins):
            if item <= upper_bound:
                if i == 0:
                    bin_key = "bin_0"
                else:
                    bin_key = f"bin_{i-1}"
                found_bin = bin_key
                break
        if found_bin:
            if found_bin not in grouped:
                grouped[found_bin] = []
            grouped[found_bin].append(item)
        else:
            pass 
    return grouped
if __name__ == '__main__':
    sample_data = [1, 5, 2, 8, 3, 9, 4, 6]
    sample_bins = [3, 6, 9]
    result = group_data(sample_data, sample_bins)
    print(result)