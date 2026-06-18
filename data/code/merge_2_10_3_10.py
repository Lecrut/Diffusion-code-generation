def sort_numbers(arr):
    return sorted(arr, key=lambda x: (x < 0, -abs(x)))
if __name__ == '__main__':
    sample_data = [-5, 3, -12, 7, 0, -8, 4]
    result = sort_numbers(sample_data)
    print(result)