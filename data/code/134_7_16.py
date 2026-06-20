def verify_exclusivity(state1, state2):
    if not (state1 == 0 or state1 == 1) or not (state2 == 0 or state2 == 1):
        raise ValueError("States must be either 0 or 1")
    return (state1 & ~state2) != 0 and (state2 & ~state1) != 0

if __name__ == '__main__':
    print(f"Verify exclusivity(0, 1): {verify_exclusivity(0, 1)}")
    print(f"Verify exclusivity(1, 0): {verify_exclusivity(1, 0)}")
    print(f"Verify exclusivity(0, 0): {verify_exclusivity(0, 0)}")
    print(f"Verify exclusivity(1, 1): {verify_exclusivity(1, 1)}")