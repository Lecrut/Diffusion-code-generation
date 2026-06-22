def compare_adjacent(data):
    result = []
    for i in range(len(data) - 1):
        if data[i] < data[i + 1]:
            result.append("ascending")
        elif data[i] > data[i + 1]:
            result.append("descending")
        else:
            result.append("equal")
    return result

if __name__ == '__main__':
    sample_list = [1.5, 2.3, 4.7, 3.6, 5.0]
    print(compare_adjacent(sample_list))