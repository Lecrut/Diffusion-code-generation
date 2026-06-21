def access_elements_by_index(sample_list):
    if not isinstance(sample_list, list):
        raise ValueError("Input must be a list")
    for index in range(len(sample_list)):
        print(f"Element at index {index}: {sample_list[index]}")

if __name__ == '__main__':
    sample_values = [100, 200, 300, 400, 500]
    access_elements_by_index(sample_values)