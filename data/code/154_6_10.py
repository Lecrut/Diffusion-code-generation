if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 1, 2]
    result = [(item, sample_list.count(item)) for item in set(sample_list)]
    print(result)