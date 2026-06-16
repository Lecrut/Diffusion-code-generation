def generate_cycled_list(seeds, cycle_length):
    result = []
    num_seeds = len(seeds)
    for i in range(cycle_length):
        index = i % num_seeds
        result.append(seeds[index])
    return result
if __name__ == '__main__':
    sample_seeds = [1, 2, 3]
    sample_cycle_length = 7
    output = generate_cycled_list(sample_seeds, sample_cycle_length)
    print(output)