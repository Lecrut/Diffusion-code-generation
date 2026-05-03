def sort_pairs(pairs):
    return sorted(pairs, key=lambda item: item[0], reverse=True)
if __name__ == '__main__':
    sample_data = [(10, 1), (5, 2), (20, 3), (15, 4)]
    sorted_result = sort_pairs(sample_data)
    print(sorted_result)