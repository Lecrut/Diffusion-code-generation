import itertools
def check_mutual_exclusivity(states):
    mutually_exclusive_pairs = []
    state_list = list(states)
    for state1, state2 in itertools.combinations(state_list, 2):
        if state1 == state2:
            continue
        if state1 in state2 or state2 in state1:
            mutually_exclusive_pairs.append((state1, state2))
    return mutually_exclusive_pairs
if __name__ == '__main__':
    defined_states = [
        "A",
        "B",
        "C",
        "D",
        "E"
    ]
    results = check_mutual_exclusivity(defined_states)
    print("Mutual Exclusivity Report:")
    if results:
        for pair in results:
            print(f"States {pair[0]} and {pair[1]} are mutually exclusive.")
    else:
        print("No mutually exclusive pairs found.")