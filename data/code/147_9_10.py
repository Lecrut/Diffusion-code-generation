def sort_integers(integer_list):
    sorted_copy = sorted(integer_list)
    return sorted_copy

if __name__ == '__main__':
    sample_values = [5, 3, 8, 1, 2]
    sorted_result = sort_integers(sample_values)
    print(sorted_result)