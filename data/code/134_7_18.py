def verify_exclusivity(state1, state2):
    if not isinstance(state1, int) or not isinstance(state2, int):
        raise ValueError("Both inputs must be integers.")
    if state1 < 0 or state1 > 1 or state2 < 0 or state2 > 1:
        raise ValueError("Inputs must be binary states (0 or 1).")
    return (state1 & ~state2) and (~state1 & state2)

if __name__ == '__main__':
    print(f"Exclusivity of (0, 1): {verify_exclusivity(0, 1)}")
    print(f"Exclusivity of (1, 0): {verify_exclusivity(1, 0)}")
    print(f"Exclusivity of (0, 0): {verify_exclusivity(0, 0)}")
    print(f"Exclusivity of (1, 1): {verify_exclusivity(1, 1)}")