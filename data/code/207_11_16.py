def find_maximum(iterable):
    return max(iterable, key=lambda x: x)

if __name__ == '__main__':
    sample_data = [7, 3, 9, 2, 5, 6]
    result = find_maximum(sample_data)
    print(result)