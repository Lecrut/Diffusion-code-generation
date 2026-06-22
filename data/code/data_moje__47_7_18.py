def mean(integers):
    if not integers:
        raise ValueError("List cannot be empty")
    total = 0
    count = 0
    for number in integers:
        total += number
        count += 1
    return total / count

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    result = mean(sample_data)
    print(result)