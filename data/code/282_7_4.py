def cumulative_sum_generator(generator):
    cumulative_sums = []
    current_sum = 0
    for number in generator:
        current_sum += number
        cumulative_sums.append(current_sum)
    return cumulative_sums
if __name__ == '__main__':
    sequence_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    generator_expression = (x for x in sequence_data)
    result = cumulative_sum_generator(generator_expression)
    print(result)