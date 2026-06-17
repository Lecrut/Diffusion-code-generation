def cumulative_sum_generator(generator):
    total = 0
    cumulative_sums = []
    for number in generator:
        total += number
        cumulative_sums.append(total)
    return cumulative_sums
if __name__ == '__main__':
    sequence_generator = (i * 2 for i in range(1, 11))
    result = cumulative_sum_generator(sequence_generator)
    print(result)