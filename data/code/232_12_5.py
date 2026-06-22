def print_incrementing_sequence():
    step = 1
    current_number = 0
    for _ in range(5):
        current_number += step
        print(current_number)
        step += 1

if __name__ == '__main__':
    print_incrementing_sequence()