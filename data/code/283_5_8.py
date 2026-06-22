MAX_VALUE = 10
MIN_VALUE = 2

def all_elements_in_range(lst):
    return all(MIN_VALUE <= x <= MAX_VALUE for x in lst)

if __name__ == '__main__':
    sample_list = [3, 5, 7, 9]
    print(all_elements_in_range(sample_list))