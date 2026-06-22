def average_of_integers(numbers):
    total = sum(numbers)
    count = len(numbers)
    if count == 0:
        return 0
    return total / count

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = average_of_integers(sample_list)
    print(result)