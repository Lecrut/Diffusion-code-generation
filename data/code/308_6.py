def count_elements(iterable):
    return sum(1 for _ in iterable)
if __name__ == '__main__':
    large_data = range(1000000)
    count = count_elements(large_data)
    print(count)