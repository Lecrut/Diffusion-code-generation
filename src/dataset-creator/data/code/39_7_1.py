def find_max_generator(data):
    return max((x for x in data), default=None)
if __name__ == '__main__':
    dataset = [10, 50, 30, 70, 20]
    result = find_max_generator(dataset)
    print(result)