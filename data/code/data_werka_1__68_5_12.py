def absolute_differences(data):
    previous = data[0]
    for current in data[1:]:
        yield abs(current - previous)
        previous = current

if __name__ == '__main__':
    sample_list = [10, 3, 6, 9, 2]
    differences = list(absolute_differences(sample_list))
    print(differences)