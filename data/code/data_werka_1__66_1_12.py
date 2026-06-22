def compare_with_successor(arr):
    if len(arr) < 2:
        print("Array has fewer than two elements.")
        return
    
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            print(f"{arr[i]} is greater than {arr[i + 1]}")
        elif arr[i] < arr[i + 1]:
            print(f"{arr[i]} is less than {arr[i + 1]}")
        else:
            print(f"{arr[i]} is equal to {arr[i + 1]}")

if __name__ == '__main__':
    sample_array = [3, 5, 2, 8, 6]
    compare_with_successor(sample_array)