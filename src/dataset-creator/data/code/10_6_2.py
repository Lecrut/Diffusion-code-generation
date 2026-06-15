def running_total_generator(data):
    current_sum = 0
    for number in data:
        current_sum += number
        yield current_sum
if __name__ == '__main__':
    sample_sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    total_generator = running_total_generator(sample_sequence)
    print(list(total_generator))