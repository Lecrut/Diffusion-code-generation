def running_total_generator(data):
    total = 0
    for item in data:
        total += item
        yield total
if __name__ == '__main__':
    sample_sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    running_totals = running_total_generator(sample_sequence)
    print(list(running_totals))