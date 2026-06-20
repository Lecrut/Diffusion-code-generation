def verify_exclusivity(state1: int, state2: int) -> bool:
    if not (state1 == 0 or state1 == 1):
        raise ValueError("State 1 must be either 0 or 1")
    if not (state2 == 0 or state2 == 1):
        raise ValueError("State 2 must be either 0 or 1")

    return (not state1) & (not state2)

if __name__ == '__main__':
    print(f"States 0 and 0: {verify_exclusivity(0, 0)}")
    print(f"States 0 and 1: {verify_exclusivity(0, 1)}")
    print(f"States 1 and 0: {verify_exclusivity(1, 0)}")
    print(f"States 1 and 1: {verify_exclusivity(1, 1)}")