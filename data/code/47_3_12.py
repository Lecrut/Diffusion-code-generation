def average(values):
    total = 0
    count = 0
    for v in values:
        total += v
        count += 1
    if count == 0:
        return 0
    return total / count

def average_generator(values):
    total = sum(v for v in values)
    count = sum(1 for v in values)
    if count == 0:
        return 0
    return total / count

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = average_generator(sample_list)
    print(result)