def get_central_element(arr):
    if not arr:
        return None
    index = len(arr) // 2
    return arr[index]

if __name__ == '__main__':
    sample_odd = [1, 3, 5, 7, 9]
    sample_even = [2, 4, 6, 8, 10, 12]
    print(get_central_element(sample_odd))
    print(get_central_element(sample_even))
    print(get_central_element([]))