def min_generator(lst):
    return (x for x in lst)

if __name__ == '__main__':
    sample_list = [34, 23, 56, 12, 89, 78]
    min_value = min(min_generator(sample_list))
    print(min_value)