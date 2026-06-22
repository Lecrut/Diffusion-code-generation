def compare_successors(arr):
    n = len(arr)
    if n < 2:
        return

    for i in range(n - 1):
        current_element = arr[i]
        next_element = arr[i + 1]

        if current_element < next_element:
            print(f"Comparison at index {i}: {current_element} < {next_element}")
        elif current_element > next_element:
            print(f"Comparison at index {i}: {current_element} > {next_element}")
        else:
            print(f"Comparison at index {i}: {current_element} == {next_element}")

if __name__ == '__main__':
    sample_array_1 = [3, 7, 2, 9, 4]
    print("--- Sample Array 1 ---")
    compare_successors(sample_array_1)

    sample_array_2 = [6, 6, 6, 6]
    print("\n--- Sample Array 2 ---")
    compare_successors(sample_array_2)