import sys
def append_elements(data_list):
    data_list.extend([10] * 5)
    return len(data_list)
if __name__ == '__main__':
    large_dataset = [i for i in range(1_000_000)]
    append_elements(large_dataset)
    append_elements(large_dataset)
    append_elements(large_dataset)
    print(f"Final dataset size: {len(large_dataset)}")