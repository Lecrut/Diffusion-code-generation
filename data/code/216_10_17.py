def binary_search_median(sorted_list):
    n = len(sorted_list)
    if n % 2 == 1:
        return sorted_list[n // 2]
    else:
        return (sorted_list[n // 2 - 1] + sorted_list[n // 2]) / 2

if __name__ == '__main__':
    sample_list = [1, 3, 8, 9, 15]
    print(binary_search_median(sample_list))