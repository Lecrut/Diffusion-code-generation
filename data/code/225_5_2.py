def compare_extremes(data_list):
    if not data_list:
        return None, None
    minimum = data_list[0]
    maximum = data_list[0]
    for item in data_list:
        if item < minimum:
            minimum = item
        if item > maximum:
            maximum = item
    return minimum, maximum
if __name__ == '__main__':
    list1 = [10, 5, 20, -3, 15]
    list2 = []
    list3 = [7.5, 1.2, 9.8, 3.3]
    list4 = [-100, 0, 50, -50]
    list5 = [42]
    print(f"List 1: {list1}")
    min1, max1 = compare_extremes(list1)
    print(f"Min: {min1}, Max: {max1}\n")
    print(f"List 2: {list2}")
    min2, max2 = compare_extremes(list2)
    print(f"Min: {min2}, Max: {max2}\n")
    print(f"List 3: {list3}")
    min3, max3 = compare_extremes(list3)
    print(f"Min: {min3}, Max: {max3}\n")
    print(f"List 4: {list4}")
    min4, max4 = compare_extremes(list4)
    print(f"Min: {min4}, Max: {max4}\n")
    print(f"List 5: {list5}")
    min5, max5 = compare_extremes(list5)
    print(f"Min: {min5}, Max: {max5}\n")