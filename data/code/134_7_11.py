def verify_exclusivity(state1, state2):
    return (state1 & ~state2) == 0 and (state2 & ~state1) == 0

if __name__ == '__main__':
    sample_state1 = 1
    sample_state2 = 0
    print(f"States: {sample_state1}, {sample_state2}")
    print(f"Mutually exclusive: {verify_exclusivity(sample_state1, sample_state2)}")