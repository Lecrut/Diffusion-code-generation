def min_generator(lst):
    for item in lst:
        yield item

if __name__ == '__main__':
    sample_list = [5, 3, 9, 1, 4]
    min_value = min(min_generator(sample_list))
    print(min_value)