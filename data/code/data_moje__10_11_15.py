def get_first_item(arr):
    if not arr:
        return None
    return arr[0]

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = []
    sample_list3 = ['apple', 'banana', 'cherry']

    result1 = get_first_item(sample_list1)
    result2 = get_first_item(sample_list2)
    result3 = get_first_item(sample_list3)

    print(result1)
    print(result2)
    print(result3)