def all_elements_equal(lst):
    return all(x == lst[0] for x in lst)

if __name__ == '__main__':
    sample_values = [True, True, True]
    print(all_elements_equal(sample_values))