def absolute_differences(data):
    return (abs(b - a) for a, b in zip(data, data[1:]))

if __name__ == '__main__':
    sample_list = [7, 3, 9, 2, 6]
    differences = list(absolute_differences(sample_list))
    print(differences)