def cycle_values(start, end, count):
    cycle = range(start, end + 1)
    results = []
    for i in range(count):
        index = i % len(cycle)
        results.append(cycle[index])
    return results
if __name__ == '__main__':
    start_val = 1
    end_val = 5
    num_cycles = 10
    cycled_values = cycle_values(start_val, end_val, num_cycles)
    print(cycled_values)