def max_value_generator(data):
    return max(item for item in data)
if __name__ == '__main__':
    large_dataset = [i * 10 ** (len(str(i))) if i < 2 else i - 5 for i in range(1, 3)] + list(range(100))
    print(max_value_generator(large_dataset))