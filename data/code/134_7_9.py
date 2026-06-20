def verify_exclusivity(state1: int, state2: int) -> bool:
    return (state1 & ~state2) == 0 and (~state1 & state2) == 0

if __name__ == '__main__':
    print(f"States 0 and 1 are mutually exclusive: {verify_exclusivity(0, 1)}")
    print(f"States 1 and 1 are mutually exclusive: {verify_exclusivity(1, 1)}")
    print(f"States 0 and 0 are mutually exclusive: {verify_exclusivity(0, 0)}")