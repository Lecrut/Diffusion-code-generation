def find_median(sample):
    n = len(sample)
    if n == 0:
        return None
    sorted_sample = quickselect(sample, n // 2)
    if n % 2 == 1:
        return sorted_sample[n // 2]
    else:
        mid1 = sorted_sample[n // 2 - 1]
        mid2 = sorted_sample[n // 2]
        return (mid1 + mid2) / 2.0

def quickselect(sample, k):
    if len(sample) == 1:
        return sample[0]

    pivot = sample[len(sample) // 2]
    left = [x for x in sample if x < pivot]
    middle = [x for x in sample if x == pivot]
    right = [x for x in sample if x > pivot]

    if k < len(left):
        return quickselect(left, k)
    elif k < len(left) + len(middle):
        return middle[0]
    else:
        return quickselect(right, k - len(left) - len(middle))

def calculate_multiple_medians(data):
    medians = []
    for sample in data:
        median = find_median(sample)
        medians.append(median)
    return medians

if __name__ == '__main__':
    samples = [
        [1, 3, 5],
        [10, 22, 9, 33, 21, 50, 41, 60, 80],
        [],
        [7]
    ]
    print(calculate_multiple_medians(samples))