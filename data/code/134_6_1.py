import itertools
def check_mutual_exclusivity(states):
    exclusive_pairs = []
    for state1, state2 in itertools.combinations(states, 2):
        if state1 == state2:
            continue
        if state1 in state2 or state2 in state1:
            exclusive_pairs.append((state1, state2))
    return exclusive_pairs
if __name__ == '__main__':
    state_definitions = [
        "A",
        "B",
        "C",
        "D",
        "E"
    ]
    results = check_mutual_exclusivity(state_definitions)
    print("Mutual Exclusivity Report:")
    if results:
        for s1, s2 in results:
            print(f"States {s1} and {s2} are mutually exclusive.")
    else:
        print("No mutually exclusive pairs found.")