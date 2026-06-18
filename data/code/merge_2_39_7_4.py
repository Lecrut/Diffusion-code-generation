def max_value_generator(data):
    return max(item for item in data)
if __name__ == '__main__':
    large_dataset = [i * 10 ** (len(str(i))) for i in range(1_000)]
    print(max_value_generator(large_dataset))