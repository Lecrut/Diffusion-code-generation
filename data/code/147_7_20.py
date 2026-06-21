def sort_large_list(items):
    return sorted(items, reverse=True)

if __name__ == '__main__':
    sample_values = [15, 20, 3, 8, 6, 25, 1, 7, 4]
    sorted_values = sort_large_list(sample_values)
    print(sorted_values)