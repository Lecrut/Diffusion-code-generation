def cumulative_sum_generator(generator):
    cumulative_sums = []
    current_sum = 0
    for number in generator:
        current_sum += number
        cumulative_sums.append(current_sum)
    return cumulative_sums
if __name__ == '__main__':
    sequence_generator = (i * 2 for i in range(10))
    result = cumulative_sum_generator(sequence_generator)
    print(result)