def average(values):
    total = sum(values)
    count = len(values)
    if count == 0:
        return 0
    return total / count

def average_with_generator(values):
    gen = (x for x in values)
    total = sum(gen)
    count = len(values)
    if count == 0:
        return 0
    return total / count

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    result = average_with_generator(sample_data)
    print(result)