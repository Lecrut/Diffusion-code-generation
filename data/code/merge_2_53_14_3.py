def count_items(data):
    return len(data)
if __name__ == '__main__':
    list_data = [10, 20, 30]
    tuple_data = (40, 50)
    print(f"List length: {count_items(list_data)}")
    print(f"Tuple length: {count_items(tuple_data)}")