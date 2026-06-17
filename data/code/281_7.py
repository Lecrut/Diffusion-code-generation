def sum_array_elements(arr):
    total = 0.0
    for element in arr:
        total += element
    return total
if __name__ == '__main__':
    sample_array = [1.5, 2.75, 3.0, -4.2, 10.1]
    result = sum_array_elements(sample_array)
    print(result)