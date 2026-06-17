def find_largest_xor(numbers):
    if not numbers:
        return None
    result = numbers[0]
    for i in range(1, len(numbers)):
        result = result ^ numbers[i]
    return result
if __name__ == '__main__':
    list1 = [10, 5, 2, 8]
    print(find_largest_xor(list1))
    list2 = [42, 17, 9, 33]
    print(find_largest_xor(list2))
    list3 = [7, 7, 7, 7]
    print(find_largest_xor(list3))
    list4 = [1, 2, 3, 4]
    print(find_largest_xor(list4))