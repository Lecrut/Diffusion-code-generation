def find_min_max(data):
    if not data:
        return None, None
    minimum = data[0]
    maximum = data[0]
    for item in data:
        if item < minimum:
            minimum = item
        if item > maximum:
            maximum = item
    return minimum, maximum
if __name__ == '__main__':
    list1 = [5, 2, 8, 1, 9]
    min1, max1 = find_min_max(list1)
    print(f"List: {list1}, Minimum: {min1}, Maximum: {max1}")
    list2 = []
    min2, max2 = find_min_max(list2)
    print(f"List: {list2}, Minimum: {min2}, Maximum: {max2}")
    list3 = [42]
    min3, max3 = find_min_max(list3)
    print(f"List: {list3}, Minimum: {min3}, Maximum: {max3}")
    list4 = [-10, -5, -20, 0]
    min4, max4 = find_min_max(list4)
    print(f"List: {list4}, Minimum: {min4}, Maximum: {max4}")