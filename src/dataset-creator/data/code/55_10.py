def swap_adjacent(items: list | tuple) -> None:
    if len(items) < 2:
        return
    for i in range(len(items) - 1):
        items[i], items[i + 1] = items[i + 1], items[i]
if __name__ == '__main__':
    data_list = [5, 3, 8, 9]
    data_tuple = (20, 40)
    swap_adjacent(data_list)
    print(f"List after swapping: {data_list}")