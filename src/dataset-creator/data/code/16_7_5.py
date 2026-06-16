def count_items(items):
    return sum(1 for _ in items)
if __name__ == '__main__':
    large_list = list(range(0, 5_000_000))
    print(count_items(large_list))