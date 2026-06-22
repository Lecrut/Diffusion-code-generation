def print_incrementing_sequence(start=1):
    step = 1
    current_number = start
    for _ in range(5):
        print(current_number)
        current_number += step
        step += 1

if __name__ == '__main__':
    print_incrementing_sequence()