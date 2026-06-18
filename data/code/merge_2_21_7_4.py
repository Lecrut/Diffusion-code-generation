import sys
def efficient_append(data_list):
    if not data_list:
        return []
    target_size = int(len(data_list) * 1.1)
    new_capacity = max(target_size, len(sys.getsizeof([data_list[0]])) // sys.maxsize if data_list else 8)
    while len(data_list) < target_size:
        current_len = len(data_list)
        chunk_size = min(1024, new_capacity - current_len)
        for i in range(chunk_size):
            data_list.append(None)                                                             
    return data_list
if __name__ == '__main__':
    large_dataset = list(range(5_000_000))
    if len(large_dataset) > 1:
        new_element = [99] * 100
        for item in new_element:
            large_dataset.append(item)
    print(f"Final size after efficient append: {len(large_dataset)}")