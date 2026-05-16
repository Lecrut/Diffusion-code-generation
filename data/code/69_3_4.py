def reverse_list_by_index(data):
    n = len(data)
    left = 0
    right = n - 1
    while left < right:
        temp = data[left]
        data[left] = data[right]
        data[right] = temp
        left += 1
        right -= 1
    return data
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(sample_list)
    reversed_list = reverse_list_by_index(sample_list)
    print(reversed_list)