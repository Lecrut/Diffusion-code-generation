def min_generator(lst):
    return (x for x in lst)

if __name__ == '__main__':
    sample_list = [3, 5, 1, 2, 4]
    min_value = min(min_generator(sample_list))
    print(min_value)