def find_median(sorted_list):
    n = len(sorted_list)
    if n % 2 == 1:
        return sorted_list[n // 2]
    else:
        mid1, mid2 = sorted_list[(n - 1) // 2], sorted_list[n // 2]
        return (mid1 + mid2) / 2

if __name__ == '__main__':
    sample_list = [1, 3, 8, 9, 15]
    print(find_median(sample_list))