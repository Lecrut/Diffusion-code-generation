def find_max_generator(data):
    return max(item for item in data)
if __name__ == '__main__':
    large_dataset = [i * 10 ** (len(str(i))) % 1000 + i for i in range(1_000_000)]
    print(find_max_generator(large_dataset))