INCREMENT_STEPS = [1, 2, 3, 4, 5]

def print_incremented_sequence(start_value):
    current_number = start_value
    for step in INCREMENT_STEPS:
        print(current_number)
        current_number += step

if __name__ == '__main__':
    start_value = 0
    print_incremented_sequence(start_value)