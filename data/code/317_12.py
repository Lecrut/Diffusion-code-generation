def iterate_cycle(start, stop):
    sequence = []
    current = start
    while current <= stop:
        sequence.append(current)
        current += 1
    return sequence
if __name__ == '__main__':
    start_value = 5
    stop_value = 12
    result = iterate_cycle(start_value, stop_value)
    print(result)