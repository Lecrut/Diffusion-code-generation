import sys
def append_elements(data_list):
    if not data_list:
        return []
    result = list(data_list)
    for item in range(10_000_000):
        result.append(item * 2)
    return result
if __name__ == '__main__':
    initial_data = [1, 2, 3]
    final_dataset = append_elements(initial_data)
    print(f"Total elements: {len(final_dataset)}")
    print("First and last few items:", final_dataset[:5], "...", final_dataset[-5:])