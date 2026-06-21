def compute_median(values):
    sorted_values = sorted(values)
    n = len(sorted_values)
    if n % 2 == 1:
        return sorted_values[n // 2]
    else:
        mid1 = sorted_values[n // 2 - 1]
        mid2 = sorted_values[n // 2]
        return (mid1 + mid2) // 2

if __name__ == '__main__':
    array1 = [3, 1, 4, 1, 5, 9, 2]
    array2 = [10, 20, 30, 40]
    array3 = [7]
    array4 = [5, 5, 5, 5]

    print(compute_median(array1))
    print(compute_median(array2))
    print(compute_median(array3))
    print(compute_median(array4))