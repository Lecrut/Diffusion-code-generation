def simulate_logic_gates():
    inputs = [
        (0, 0),
        (0, 1),
        (1, 0),
        (1, 1)
    ]
    print("--- AND Gate Simulation ---")
    for a, b in inputs:
        result = a & b
        print(f"AND({a}, {b}) = {result}")
    print("\n--- OR Gate Simulation ---")
    for a, b in inputs:
        result = a | b
        print(f"OR({a}, {b}) = {result}")
    print("\n--- NOT Gate Simulation ---")
    for a, b in inputs:
        not_a = not a
        not_b = not b
        print(f"NOT({a}) = {not_a}")
        print(f"NOT({b}) = {not_b}")
if __name__ == '__main__':
    simulate_logic_gates()