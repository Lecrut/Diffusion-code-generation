def average_generator(data):
    total = 0
    count = 0
    for item in data:
        total += item
        count += 1
        yield total / count
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    avg_gen = average_generator(sample_list)
    print(list(avg_gen))