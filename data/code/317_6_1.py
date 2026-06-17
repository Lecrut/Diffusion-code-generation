def cycle_values(start, end, count):
    current = start
    for _ in range(count):
        current = (current - 1) % (end - start + 1) + start
        print(current)
if __name__ == '__main__':
    start_val = 1
    end_val = 5
    num_cycles = 10
    cycle_values(start_val, end_val, num_cycles)