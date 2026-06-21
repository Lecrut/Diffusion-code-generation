def sort_integers(int_list):
    if not int_list:
        return []
    return sorted(int_list)

if __name__ == '__main__':
    sample_values = [34, 7, 23, 32, 5, 62]
    sorted_values = sort_integers(sample_values)
    print(sorted_values)