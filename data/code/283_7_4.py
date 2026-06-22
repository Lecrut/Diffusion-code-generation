def all_elements_equal(lst):
    return len(set(lst)) == 1

if __name__ == '__main__':
    print(all_elements_equal([1, 1, 1]))
    print(all_elements_equal(['a', 'a', 'b']))
    print(all_elements_equal([]))
    print(all_elements_equal([True, True, True]))