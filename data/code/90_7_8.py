def simulate_boolean_logic(a, b, c):
    return (a or b) and (b or c)

if __name__ == '__main__':
    result = simulate_boolean_logic(True, False, True)
    print(result)