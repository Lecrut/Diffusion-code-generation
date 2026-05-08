import itertools
def check_mutual_exclusivity(states):
    mutually_exclusive_pairs = []
    state_list = list(states)
    n = len(state_list)
    for i in range(n):
        for j in range(i + 1, n):
            state1 = state_list[i]
            state2 = state_list[j]
            if state1 == state2:
                mutually_exclusive_pairs.append((state1, state2))
    return mutually_exclusive_pairs
if __name__ == '__main__':
    state_definitions = [
        "StateA",
        "StateB",
        "StateC",
        "StateA",
        "StateD",
        "StateB"
    ]
    results = check_mutual_exclusivity(state_definitions)
    print("Mutually Exclusive Pairs:")
    for pair in results:
        print(pair)