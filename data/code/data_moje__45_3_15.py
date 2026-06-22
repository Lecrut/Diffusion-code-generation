def get_minimum(values):
    return min([x for x in values])

if __name__ == '__main__':
    sample_list = [10, 5, 8, 20, 1]
    result = get_minimum(sample_list)
    print(result)