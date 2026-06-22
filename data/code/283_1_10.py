def are_all_integers(lst):
    return all(isinstance(item, int) for item in lst)

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(are_all_integers(sample_list))