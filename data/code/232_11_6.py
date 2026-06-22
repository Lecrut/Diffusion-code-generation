def generate_growing_sequence():
    current_term = 1
    for _ in range(5):
        print(current_term)
        current_term *= 2

if __name__ == '__main__':
    generate_growing_sequence()