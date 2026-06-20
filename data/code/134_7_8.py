def verify_exclusivity(state1, state2):
    return state1 & ~state2 == 0 and state2 & ~state1 == 0
if __name__ == '__main__':
    print(verify_exclusivity(0, 1))
    print(verify_exclusivity(1, 0))
    print(verify_exclusivity(0, 0))
    print(verify_exclusivity(1, 1))