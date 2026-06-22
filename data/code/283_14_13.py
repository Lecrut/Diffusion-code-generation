def all_even(lst):
    return all(x % 2 == 0 for x in lst)

if __name__ == '__main__':
    sample = [2, 4, 6, 8]
    print(all_even(sample))