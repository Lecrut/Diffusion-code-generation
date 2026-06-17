def cycle_values(start=1, end=5, repetitions=10):
    current_value = start
    for i in range(repetitions):
        print(current_value)
        current_value = (current_value % (end - start + 1)) + start
if __name__ == '__main__':
    cycle_values()