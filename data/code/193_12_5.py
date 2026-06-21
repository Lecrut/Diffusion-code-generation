def aggregate_numeric_values(lst):
    return sum(filter(lambda x: isinstance(x, (int, float)), lst))

if __name__ == '__main__':
    sample_list = [1, 2, 'a', 3.5, None, 4]
    print(aggregate_numeric_values(sample_list))