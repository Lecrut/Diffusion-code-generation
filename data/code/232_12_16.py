def print_incrementing_sequence():
    step = 1
    current_number = 0
    for _ in range(5):
        print(current_number)
        current_number += step
        step += 1

if __name__ == '__main__':
    print_incrementing_sequence()