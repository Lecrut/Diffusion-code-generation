def simulate_boolean_logic(var1, var2, var3):
    return (var1 or var2) and (not var3)

if __name__ == '__main__':
    result = simulate_boolean_logic(True, False, True)
    print(result)