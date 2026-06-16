def cycle_iterator(start, stop):
    sequence = []
    current = start
    while current <= stop:
        sequence.append(current)
        current += 1
    return sequence
if __name__ == '__main__':
    start_value = 5
    stop_value = 10
    result_list = cycle_iterator(start_value, stop_value)
    print(result_list)