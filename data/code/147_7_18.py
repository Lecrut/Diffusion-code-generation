def sort_large_list(items):
    return sorted(items, reverse=True)

if __name__ == '__main__':
    sample_values = [5, 3, 8, 4, 2]
    print(sort_large_list(sample_values))