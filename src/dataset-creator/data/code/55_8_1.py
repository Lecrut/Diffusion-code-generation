def swap_neighbors(data_list):
    if len(data_list) < 2:
        return data_list
    index = None
    def get_index():
        nonlocal index
        if index is None:
            index = int(input("Enter the starting index of neighbors (0-based): "))
    while True:
        try:
            get_index()
            if 0 <= index < len(data_list) - 1:
                data_list[index], data_list[index + 1] = data_list[index + 1], data_list[index]
                print("Swap completed successfully.")
                return
            else:
                print(f"Error: Index {index} is out of range for a pair. Valid range: 0 to {len(data_list) - 2}")
        except ValueError:
            print("Invalid input. Please enter an integer.")
if __name__ == '__main__':
    sample_data = [1, 5, 3, 9, 7]
    dataset = [10, 25, 30, 45]
    start_index = 0
    if len(dataset) > start_index + 1:
        dataset[start_index], dataset[start_index + 1] = dataset[start_index + 1], dataset[start_index]
if __name__ == '__main__':
    print(f"Original list: {dataset}")