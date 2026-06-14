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
    list1 = [1, 5, 2, 8, 3]
    print(f"List: {list1}, Min: {compare_extremes(list1)}, Max: {compare_extremes(list1)}")
    list2 = [-10, 0, 5, -20]
    print(f"List: {list2}, Min: {compare_extremes(list2)}, Max: {compare_extremes(list2)}")
    list3 = []
    print(f"List: {list3}, Min: {compare_extremes(list3)}, Max: {compare_extremes(list3)}")
    list4 = [42]
    print(f"List: {list4}, Min: {compare_extremes(list4)}, Max: {compare_extremes(list4)}")
    list5 = ["apple", "banana", "cherry"]
    print(f"List: {list5}, Min: {compare_extremes(list5)}, Max: {compare_extremes(list5)}")
    list6 = [3.14, 1.618, 2.718]
    print(f"List: {list6}, Min: {compare_extremes(list6)}, Max: {compare_extremes(list6)}")