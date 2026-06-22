def compare_successors(arr):
    if len(arr) < 2:
        return
    for index in range(len(arr) - 1):
        current = arr[index]
        next_element = arr[index + 1]
        if current < next_element:
            print(f"Index {index}: {current} is less than {next_element}")
        elif current > next_element:
            print(f"Index {index}: {current} is greater than {next_element}")
        else:
            print(f"Index {index}: {current} is equal to {next_element}")

if __name__ == '__main__':
    sample_array1 = [7, 3, 9, 3, 5]
    print("--- Sample Array 1 ---")
    compare_successors(sample_array1)
    
    sample_array2 = [4, 4, 4, 4]
    print("\n--- Sample Array 2 ---")
    compare_successors(sample_array2)