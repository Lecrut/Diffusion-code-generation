import math

STEP_SIZE = 10

def group_by_bins(data):
    bins = {}
    for number in data:
        bin_start = int(math.floor(number / STEP_SIZE)) * STEP_SIZE
        if bin_start not in bins:
            bins[bin_start] = []
        bins[bin_start].append(number)
    return bins

if __name__ == '__main__':
    sample_data = [5, 12, 17, 23, 34, 40, 48, 55, 61, 69]
    grouped_bins = group_by_bins(sample_data)
    print(grouped_bins)