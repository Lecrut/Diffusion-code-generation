def timsort(arr):
    return sorted(arr)

if __name__ == '__main__':
    sample_values = [34, 7, 23, 32, 5, 62]
    print(timsort(sample_values))
    print(timsort([]))
    print(timsort([1, 1, 1, 1]))