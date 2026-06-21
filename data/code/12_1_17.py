import math

def find_median(lst):
    if not lst:
        raise ValueError("List must not be empty")
    sorted_list = sorted(lst)
    n = len(sorted_list)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_list[mid - 1] + sorted_list[mid]) / 2
    return sorted_list[mid]

if __name__ == '__main__':
    data = [12, 4, 5, 3, 7, 9, 1, 8]
    result = find_median(data)
    print(result)