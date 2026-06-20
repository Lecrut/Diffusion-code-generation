def and_operation(state1, state2):
    return state1 and state2

if __name__ == '__main__':
    sample_state1 = True
    sample_state2 = False
    result = and_operation(sample_state1, sample_state2)
    print(f"Result of AND operation between {sample_state1} and {sample_state2}: {result}")