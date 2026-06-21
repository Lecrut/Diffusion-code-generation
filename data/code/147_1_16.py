def optimized_in_place_sort(strings):
    n = len(strings)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if strings[j] < strings[min_idx]:
                min_idx = j
        strings[i], strings[min_idx] = strings[min_idx], strings[i]

if __name__ == '__main__':
    sample_strings = ["cherry", "banana", "date", "apple"]
    optimized_in_place_sort(sample_strings)
    print(sample_strings)