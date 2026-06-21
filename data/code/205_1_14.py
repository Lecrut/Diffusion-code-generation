def validate_input(data):
    if not all(isinstance(x, float) for x in data):
        raise ValueError("All elements must be floating-point numbers")

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

if __name__ == '__main__':
    sample_values = [3.5, 2.1, 4.8, 1.9, 5.6]
    validate_input(sample_values)
    sorted_values = bubble_sort(sample_values)
    print(sorted_values)