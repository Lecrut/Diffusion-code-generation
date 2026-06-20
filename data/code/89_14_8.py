def and_operation(state1, state2):
    operations = {
        True: {True: True, False: False},
        False: {True: False, False: False}
    }
    return operations[state1][state2]

if __name__ == '__main__':
    state1 = True
    state2 = False
    result = and_operation(state1, state2)
    print(f"Result of AND operation on {state1} and {state2}: {result}")