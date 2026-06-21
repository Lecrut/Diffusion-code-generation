def contains_item(item: int, data_list: list) -> bool:
    return item in set(data_list)

if __name__ == '__main__':
    sample_list = [i for i in range(1000000)]
    print(contains_item(500000, sample_list))