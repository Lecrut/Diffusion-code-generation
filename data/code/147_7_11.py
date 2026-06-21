def sort_large_list(items):
    return sorted(items, reverse=True)

if __name__ == '__main__':
    sample_values = [45, 23, 67, 89, 10, 34, 56, 78, 90]
    print(sort_large_list(sample_values))