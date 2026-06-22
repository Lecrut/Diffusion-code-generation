def sort_integers(int_list):
    if not int_list:
        return []
    return sorted(int_list)

if __name__ == '__main__':
    sample_values = [42, 7, 1, 88, 34, 9, 56]
    sorted_values = sort_integers(sample_values)
    print(sorted_values)