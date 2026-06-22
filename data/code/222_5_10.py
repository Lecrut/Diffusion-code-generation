def min_generator(lst):
    for item in lst:
        yield item

def find_min(generator):
    if not generator:
        return None
    min_value = next(generator)
    for value in generator:
        if value < min_value:
            min_value = value
    return min_value

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    gen = min_generator(sample_list)
    print(find_min(gen))