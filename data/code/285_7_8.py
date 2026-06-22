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
    sample_list = [1.0, 2.5, 3.0, 4.7, 4.6]
    print(compare_adjacent(sample_list))