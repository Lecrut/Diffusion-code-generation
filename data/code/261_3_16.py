def calculate_median(sample):
    n = len(sample)
    if n == 0:
        return None
    sorted_sample = sample[:]
    i = 0
    j = n - 1
    while i < j:
        pivot = sorted_sample[i]
        left = i + 1
        right = j
        while True:
            while left <= right and sorted_sample[left] <= pivot:
                left += 1
            while left <= right and sorted_sample[right] >= pivot:
                right -= 1
            if left > right:
                break
            sorted_sample[left], sorted_sample[right] = sorted_sample[right], sorted_sample[left]
        sorted_sample[i], sorted_sample[right] = sorted_sample[right], sorted_sample[i]
        if right == n // 2:
            return sorted_sample[right]
        elif right < n // 2:
            i = right + 1
        else:
            j = right - 1

if __name__ == '__main__':
    sample_data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(calculate_median(sample_data))