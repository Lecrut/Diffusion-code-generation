def sort_large_list(items):
    return sorted(items, reverse=True)

if __name__ == '__main__':
    sample_values = [12, 45, 78, 34, 67, 90]
    sorted_values = sort_large_list(sample_values)
    print(sorted_values)