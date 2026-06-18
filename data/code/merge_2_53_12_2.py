def count_items(data):
    return len([item for item in data])
if __name__ == '__main__':
    sample_data = list(range(10_000_000))
    result = count_items(sample_data)
    print(result)