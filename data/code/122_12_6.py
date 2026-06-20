def compute_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    if count == 0:
        return 0
    return total / count

if __name__ == '__main__':
    sample_data = [5, 15, 25, 35, 45]
    avg = compute_average(sample_data)
    print(avg)