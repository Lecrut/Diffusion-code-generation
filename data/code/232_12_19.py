def print_incrementing_sequence():
    current_number = 0
    step_size = 1
    for _ in range(5):
        print(current_number)
        current_number += step_size
        step_size += 1

if __name__ == '__main__':
    print_incrementing_sequence()