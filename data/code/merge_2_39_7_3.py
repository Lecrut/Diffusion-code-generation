def max_generator(data):
    return max(item for item in data) if data else None
if __name__ == '__main__':
    large_dataset = [i * 10 ** (len(str(i))) for i in range(5)] + list(range(1, 2))
    print(max_generator(large_dataset))