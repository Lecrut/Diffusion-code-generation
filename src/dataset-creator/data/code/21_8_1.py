def append_heterogeneous_data(target_list: list) -> None:
    samples = [1, "text", {"key": "value"}, [10, 20], True]
    print("Appending heterogeneous data to collection...")
    for item in samples:
        target_list.append(item)
    return target_list
if __name__ == '__main__':
    my_collection = []
    updated_collection = append_heterogeneous_data(my_collection)
    print("Final Collection:", updated_collection)