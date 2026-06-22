import heapq

def find_median(data):
    n = len(data)
    if n == 0:
        raise ValueError('Input list cannot be empty')

    def get_kth_largest(k, nums):
        return heapq.nlargest(k, nums)[-1]
    if n % 2 == 1:
        median = get_kth_largest(n // 2 + 1, data)
    else:
        mid1 = get_kth_largest(n // 2, data)
        mid2 = get_kth_largest(n // 2 + 1, data)
        median = (mid1 + mid2) / 2.0
    return median
if __name__ == '__main__':
    list1 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(f'Median of {list1}: {find_median(list1)}')