def memory_efficient_iterator(data_source):
    for item in data_source:
        yield item[0], item[1]
if __name__ == '__main__':
    sample_data = [
        ('apple', 5),
        ('banana', 3),
        ('cherry', 7)
    ]
    result_dict = {}
    for key, value in memory_efficient_iterator(sample_data):
        result_dict[key] = value
    print(result_dict)