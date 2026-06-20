def simulate_boolean_logic(a, b, c):
    return (a or b) or c
if __name__ == '__main__':
    print(simulate_boolean_logic(True, False, True))
    print(simulate_boolean_logic(False, False, False))