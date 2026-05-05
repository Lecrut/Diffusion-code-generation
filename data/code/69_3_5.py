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
    print(f"Original list: {sample_list}")
    reversed_list = reverse_list_by_index(sample_list)
    print(f"Reversed list: {reversed_list}")
    sample_list_2 = ['a', 'b', 'c', 'd', 'e']
    print(f"Original list: {sample_list_2}")
    reversed_list_2 = reverse_list_by_index(sample_list_2)
    print(f"Reversed list: {reversed_list_2}")
    sample_list_3 = [10, 20, 30]
    print(f"Original list: {sample_list_3}")
    reversed_list_3 = reverse_list_by_index(sample_list_3)
    print(f"Reversed list: {reversed_list_3}")