def all_elements_equal(lst):
    return len(set(lst)) == 1

if __name__ == '__main__':
    sample_list = [5, 5, 5, 5]
    print(all_elements_equal(sample_list))