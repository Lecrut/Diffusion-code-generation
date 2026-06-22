def find_maximum_via_generator(sequence):
    current_peak = None
    for element in sequence:
        if current_peak is None or element > current_peak:
            current_peak = element
    yield current_peak

if __name__ == '__main__':
    hard_coded_values = [15, 29, 8, 42, 33, 101, 7, 99, 50, 60]
    max_result = None
    for item in find_maximum_via_generator(hard_coded_values):
        max_result = item
    print(max_result)