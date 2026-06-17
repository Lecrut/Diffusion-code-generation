def calculate_cumulative_sum(generator):
    cumulative_sum = 0
    results = []
    for number in generator:
        cumulative_sum += number
        results.append(cumulative_sum)
    return results
if __name__ == '__main__':
    sequence_generator = (i * 2 for i in range(10))
    cumulative_sums = calculate_cumulative_sum(sequence_generator)
    print(cumulative_sums)