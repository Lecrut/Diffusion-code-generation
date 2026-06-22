def mean_of_integers(data):
    if not data:
        return 0
    total = 0
    for value in data:
        total += value
    return total / len(data)

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    result = mean_of_integers(sample_data)
    print(result)