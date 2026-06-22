def mean_of_integers(numbers):
    total = sum(numbers)
    count = len(numbers)
    return total / count

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    result = mean_of_integers(sample_values)
    print(result)