def sort_tuples_desc(tuples):
    return sorted(tuples, key=lambda x: x[1], reverse=True)

if __name__ == '__main__':
    sample_list = [(4, 2), (1, 3), (3, 1), (2, 4)]
    sorted_list = sort_tuples_desc(sample_list)
    print(sorted_list)