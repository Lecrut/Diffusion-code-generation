def absolute_differences(data):
    previous_value = None
    for value in data:
        if previous_value is not None:
            yield abs(value - previous_value)
        previous_value = value

if __name__ == '__main__':
    sample_list = [10, 3, 7, 2, 5]
    differences = list(absolute_differences(sample_list))
    print(differences)