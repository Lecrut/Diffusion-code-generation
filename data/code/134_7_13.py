def verify_exclusivity(state1, state2):
    return (state1 & ~state2) == 0 and (state2 & ~state1) == 0

if __name__ == '__main__':
    print(f"Exclusivity of (0, 0): {verify_exclusivity(0, 0)}")
    print(f"Exclusivity of (0, 1): {verify_exclusivity(0, 1)}")
    print(f"Exclusivity of (1, 0): {verify_exclusivity(1, 0)}")
    print(f"Exclusivity of (1, 1): {verify_exclusivity(1, 1)}")