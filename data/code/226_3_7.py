def flatten_and_repeat(tup):
    return [x for x in tup] * 5

if __name__ == '__main__':
    sample_tuple = (1, 2, 3)
    print(flatten_and_repeat(sample_tuple))