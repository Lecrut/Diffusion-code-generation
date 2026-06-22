FIBONACCI_LIMIT = 10
START_A = 0
START_B = 1

def generate_fibonacci_sequence():
    current_a = START_A
    current_b = START_B
    for _ in range(FIBONACCI_LIMIT):
        yield current_a
        current_a, current_b = current_b, current_a + current_b

def format_fibonacci_list(values):
    return ", ".join(str(val) for val in values)

if __name__ == '__main__':
    sequence_values = list(generate_fibonacci_sequence())
    formatted_output = format_fibonacci_list(sequence_values)
    print(formatted_output)