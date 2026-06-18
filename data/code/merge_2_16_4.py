def count_elements(data):
    return len(data)
if __name__ == '__main__':
    large_dataset = list(range(10_000_000))
    total_count = count_elements(large_dataset)
    print(total_count)