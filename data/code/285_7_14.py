def compare_adjacent(data):
    result = []
    for i in range(len(data) - 1):
        if data[i] < data[i + 1]:
            result.append('Ascending')
        elif data[i] > data[i + 1]:
            result.append('Descending')
        else:
            result.append('Equal')
    return result

if __name__ == '__main__':
    list1 = [1, 2.5, 3, 4.7]
    list2 = [10, 20, 30]
    list3 = [1.1, 2.2, 3.3]
    list4 = [1, "two", 3]

    print("Testing list1:", compare_adjacent(list1))
    print("Testing list2:", compare_adjacent(list2))
    print("Testing list3:", compare_adjacent(list3))
    print("Testing list4:", compare_adjacent(list4))