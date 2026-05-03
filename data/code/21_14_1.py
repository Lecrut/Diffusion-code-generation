def sort_pairs(pairs):
    return sorted(pairs, key=lambda item: item[0], reverse=True)
if __name__ == '__main__':
    sample_data = [(3, 1), (1, 5), (4, 2), (2, 8)]
    sorted_result = sort_pairs(sample_data)
    print(sorted_result)