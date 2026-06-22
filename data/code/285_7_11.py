def compare_adjacent(data):
    result = []
    for i in range(len(data) - 1):
        if data[i] < data[i + 1]:
            result.append("Ascending")
        elif data[i] > data[i + 1]:
            result.append("Descending")
        else:
            result.append("Equal")
    return result

if __name__ == '__main__':
    list1 = [1.0, 2.5, 3.0, 4.7]
    list2 = [10, 9, 8, 7]
    list3 = [1.1, 1.1, 2.2, 2.2]

    print(compare_adjacent(list1))
    print(compare_adjacent(list2))
    print(compare_adjacent(list3))