import sys
def append_to_list(data):
    if not isinstance(data, list):
        data = [data]
    result = []
    for item in data:
        if isinstance(item, (list, tuple)):
            result.extend(list(item))
        else:
            result.append(item)
    return result
if __name__ == '__main__':
    large_dataset = list(range(10_000_000))
    new_elements = [i * 2 for i in range(5)]
    final_data = append_to_list(large_dataset + new_elements)
    print(f"Original size: {len(large_dataset)}")
    print(f"New elements count: {len(new_elements)}")
    print(f"Final dataset length: {len(final_data)}")