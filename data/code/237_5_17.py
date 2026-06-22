sequence_map = {n: n**2 + n for n in range(1, 11)}

def print_sequence():
    for n, value in sequence_map.items():
        print(f"{n}: {value}")

if __name__ == '__main__':
    print_sequence()