def sort_large_list(items):
    return sorted(items, reverse=True)

if __name__ == '__main__':
    sample_values = [5, 2, 9, 1, 5, 6]
    print(sort_large_list(sample_values))