def compare_adjacent(data):
    result = []
    for i in range(len(data) - 1):
        if data[i] < data[i+1]:
            result.append("ascending")
        elif data[i] > data[i+1]:
            result.append("descending")
        else:
            result.append("equal")
    return result

if __name__ == '__main__':
    test_data = [1.1, 2.2, 3.3, 4.4, 5.5]
    print(compare_adjacent(test_data))