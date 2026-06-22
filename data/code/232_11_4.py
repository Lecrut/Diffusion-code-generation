def generate_sequence():
    current_value = 1
    for _ in range(5):
        print(current_value)
        current_value *= 2

if __name__ == '__main__':
    generate_sequence()