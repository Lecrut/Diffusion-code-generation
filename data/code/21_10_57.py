def sort_integers(int_list):
    if not int_list:
        return []
    return sorted(int_list)

if __name__ == '__main__':
    sample_values = [13, 1, 4, 12, 8, 6, 9, 2]
    sorted_values = sort_integers(sample_values)
    print(sorted_values)