def all_even(lst):
    return all(x % 2 == 0 for x in lst)

if __name__ == '__main__':
    print(all_even([2, 4, 6, 8]))
    print(all_even([1, 3, 5, 7]))