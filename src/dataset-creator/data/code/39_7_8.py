def find_max_generator(data):
    return max((x for x in data), default=None)
if __name__ == '__main__':
    dataset = [10, 50, 23, 89, 45, 67]
    print(find_max_generator(dataset))