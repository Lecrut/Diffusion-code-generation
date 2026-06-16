def generate_cycled_list(seeds, cycle_length):
    result = []
    num_seeds = len(seeds)
    for i in range(cycle_length):
        index = i % num_seeds
        result.append(seeds[index])
    return result
if __name__ == '__main__':
    seeds_list = [1, 2, 3]
    cycle_len = 7
    output = generate_cycled_list(seeds_list, cycle_len)
    print(output)