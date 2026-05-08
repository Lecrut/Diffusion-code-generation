def pairwise_differences(data):
    n = len(data)
    for i in range(n):
        for j in range(i + 1, n):
            yield data[j] - data[i]
if __name__ == '__main__':
    input_list = [1, 5, 2, 8]
    differences = list(pairwise_differences(input_list))
    print(differences)