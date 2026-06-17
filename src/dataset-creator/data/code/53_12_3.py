def count_items_from_start(data):
    return len([x for x in data])
if __name__ == '__main__':
    sample_data = list(range(10_000_000))
    result = count_items_from_start(sample_data)
    print(result)