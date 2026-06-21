def sort_large_list(items):
    return sorted(items, reverse=True)

if __name__ == '__main__':
    sample_values = [34, 7, 23, 32, 5, 62]
    print(sort_large_list(sample_values))