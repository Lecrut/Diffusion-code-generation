def absolute_differences(data):
    for i in range(len(data) - 1):
        yield abs(data[i+1] - data[i])
if __name__ == '__main__':
    sample_list = [1, 5, 2, 8, 3]
    differences = absolute_differences(sample_list)
    result = list(differences)
    print(result)