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
                break
        if not found:
            for upper_bound in bins:
                if item > upper_bound:
                    pass
            if not bins:
                grouped["overflow"] = [item]
            else:
                if not grouped:
                    grouped["overflow"] = [item]
    final_grouped = {}
    for item in data:
        assigned = False
        for upper_bound in sorted(bins):
            if item <= upper_bound:
                bin_key = upper_bound
                if bin_key not in final_grouped:
                    final_grouped[bin_key] = []
                final_grouped[bin_key].append(item)
                assigned = True
                break
        if not assigned and bins:
            final_grouped[bins[-1]] = final_grouped.get(bins[-1], []) + [item]
        elif not assigned and not bins:
             if not final_grouped:
                 final_grouped["unbounded"] = [item]
    return final_grouped
if __name__ == '__main__':
    sample_data = [10, 5, 22, 3, 15, 8, 25, 1, 12, 20]
    sample_bins = [10, 20, 30]
    result = group_data(sample_data, sample_bins)
    print(result)