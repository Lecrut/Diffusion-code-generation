def integer_exists(lst, num):
    return num in lst
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(integer_exists(sample_list, 3))
    print(integer_exists(sample_list, 6))
    print(integer_exists([], 1))