if __name__ == '__main__':
    data = [1, 3, 2, 5, 4]
    comparison_results = [data[i] <= data[i+1] for i in range(len(data) - 1)]
    print(comparison_results)