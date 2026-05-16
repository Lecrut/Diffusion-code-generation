import math
def bin_data(data, bins):
    if not bins:
        return []
    bin_edges = [data[0]]
    for i in range(1, len(data)):
        bin_edges.append(data[i])
    unique_edges = sorted(list(set(bin_edges)))
    if len(unique_edges) < 2:
        return []
    bins_result = []
    for i in range(len(unique_edges) - 1):
        lower_bound = unique_edges[i]
        upper_bound = unique_edges[i+1]
        if lower_bound < upper_bound:
            bin_start = lower_bound
            bin_end = upper_bound
            bin_data_list = []
            for x in data:
                if bin_start <= x < bin_end:
                    bin_data_list.append(x)
            if bin_data_list:
                bins_result.append({
                    "range": (bin_start, bin_end),
                    "data": bin_data_list
                })
    return bins_result
if __name__ == '__main__':
    sample_data = [1, 4, 2, 5, 8, 3, 7, 9, 10, 12]
    sample_bins = [2, 5, 8, 10]
    result = bin_data(sample_data, sample_bins)
    print(result)