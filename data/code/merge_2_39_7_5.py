def max_in_generator(data):
    return max(item for item in data)
if __name__ == '__main__':
    dataset = [i * 10 ** i for i in range(20)]
    print(max(dataset))