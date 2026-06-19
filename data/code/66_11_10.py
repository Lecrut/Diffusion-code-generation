def find_violating_pairs(arr):
    violating_elements = []
    for i in range(len(arr) - 1):
        if arr[i+1] < arr[i]:
            violating_elements.append(arr[i+1])
    return violating_elements

if __name__ == '__main__':
    sample_array = [1, 3, 2, 5, 4, 6, 7]
    result = find_violating_pairs(sample_array)
    print(result)