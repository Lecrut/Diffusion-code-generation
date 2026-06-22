def are_all_integers(lst):
    return all(isinstance(x, int) for x in lst)

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = are_all_integers(sample_list)
    print(result)