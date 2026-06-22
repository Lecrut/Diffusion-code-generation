def all_elements_equal(lst):
    return len(set(lst)) == 1

if __name__ == '__main__':
    sample_list = [3, 3, 3, 3]
    print(all_elements_equal(sample_list))