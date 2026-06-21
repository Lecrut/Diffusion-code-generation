def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break

def validate_input(data):
    if not isinstance(data, list):
        raise ValueError("Input must be a list.")
    if len(data) > 20:
        raise ValueError("List size must be 20 or less for optimal performance.")
    for item in data:
        if not isinstance(item, (int, float)):
            raise ValueError("All elements must be numbers.")

if __name__ == '__main__':
    sample_values = [3.5, 2.1, 4.8, 1.9, 5.6]
    validate_input(sample_values)
    sorted_values = bubble_sort(sample_values)
    print(sorted_values)