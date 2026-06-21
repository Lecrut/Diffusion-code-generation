def average_generator(sample):
    return sum(x for x in sample) / len(sample)

if __name__ == '__main__':
    sample_data = [50, 60, 70]
    avg_result = average_generator(sample_data)
    print(avg_result)