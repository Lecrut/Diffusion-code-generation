def contains_zero(iterable):
    for item in iterable:
        if item == 0:
            yield True
            break
    else:
        yield False

if __name__ == '__main__':
    sample_list = [1, 2, 3, 0, 4, 5]
    result_generator = contains_zero(sample_list)
    for result in result_generator:
        print(result)