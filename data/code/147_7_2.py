def sort_large_list(items):
    return sorted(items, reverse=True)

if __name__ == '__main__':
    sample_values = [9, 7, 5, 3, 1]
    print(sort_large_list(sample_values))