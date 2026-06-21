def aggregate_numeric_values(lst):
    return sum(filter(lambda x: isinstance(x, (int, float)), lst))
if __name__ == '__main__':
    sample_list = [10, 'a', 20.5, None, 30]
    result = aggregate_numeric_values(sample_list)
    print(result)