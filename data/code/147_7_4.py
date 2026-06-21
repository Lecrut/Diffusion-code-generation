def sort_large_list(items):
    return sorted(items, reverse=True)

if __name__ == '__main__':
    sample_values = [10, 34, 56, 78, 90, 23, 45, 67, 89]
    sorted_values = sort_large_list(sample_values)
    print(sorted_values)