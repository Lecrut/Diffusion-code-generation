import sys
def efficient_append(data_list):
    data_list.extend([10] * 5)
    return len(data_list), id(data_list)
if __name__ == '__main__':
    large_dataset = list(range(1_000_000))
    original_len, new_id = efficient_append(large_dataset)
    print(f"New length: {original_len}")
    print(f"List ID (no copy): {new_id} == id(large_dataset): {id(large_dataset)}")