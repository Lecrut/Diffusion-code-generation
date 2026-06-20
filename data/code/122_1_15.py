def average_generator(data):
    return sum(x for x in data) / len(data)

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    print(average_generator(sample_data))