def validate_input(data):
    if not all(isinstance(x, float) for x in data):
        raise ValueError("All elements must be floating-point numbers.")

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key > arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def sort_small_list(data):
    validate_input(data)
    insertion_sort(data)
    return data

if __name__ == '__main__':
    sample_values = [3.5, 2.1, 4.8, 1.9, 5.6]
    sorted_values = sort_small_list(sample_values)
    print(sorted_values)