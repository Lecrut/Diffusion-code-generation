def regex_to_nfa(regex):
    nfa = {}
    states = set()
    transitions = []
    start_state = 0
    accept_states = set()

    def add_transition(from_state, char, to_state):
        transitions.append((from_state, char, to_state))
    nfa[start_state] = {}
    states.add(start_state)
    return (nfa, states, transitions, start_state, accept_states)

def convert_nfa_to_dfa(nfa, states, transitions, start_state, accept_states):
    dfa = {}
    current_dfa_state = 0
    queue = [frozenset([start_state])]
    visited = set()
    while queue:
        current_nfa_states = queue.pop(0)
        if current_nfa_states not in visited:
            visited.add(current_nfa_states)
            dfa[current_dfa_state] = {}
            for char in 'abc':
                next_nfa_states = set()
                for state in current_nfa_states:
                    if state in nfa and char in nfa[state]:
                        next_nfa_states.update(nfa[state][char])
                dfa[current_dfa_state][char] = frozenset(next_nfa_states)
                if next_nfa_states:
                    queue.append(frozenset(next_nfa_states))
            current_dfa_state += 1
    return dfa

def is_isomorphic(dfa1, dfa2):
    if len(dfa1) != len(dfa2):
        return False
    state_mapping = {}
    stack = [(frozenset(dfa1.keys()), frozenset(dfa2.keys()))]
    visited = set()
    while stack:
        dfa1_states, dfa2_states = stack.pop(0)
        if (dfa1_states, dfa2_states) in visited:
            continue
        visited.add((dfa1_states, dfa2_states))
        for char in 'abc':
            next_dfa1_states = {frozenset((dfa1_state[char] for dfa1_state in dfa1_states if char in dfa1_state)) for dfa1_state in dfa1_states}
            next_dfa2_states = {frozenset((dfa2_state[char] for dfa2_state in dfa2_states if char in dfa2_state)) for dfa2_state in dfa2_states}
            if len(next_dfa1_states) != len(next_dfa2_states):
                return False
            for next_dfa1_state, next_dfa2_state in zip(sorted(next_dfa1_states), sorted(next_dfa2_states)):
                if next_dfa1_state not in state_mapping:
                    state_mapping[next_dfa1_state] = next_dfa2_state
                elif state_mapping[next_dfa1_state] != next_dfa2_state:
                    return False
                stack.append((next_dfa1_state, next_dfa2_state))
    return True
if __name__ == '__main__':
    regex1 = 'ab|ba'
    regex2 = '(a|b)(a|b)'
    dfa1, states1, transitions1, start_state1, accept_states1 = regex_to_nfa(regex1)
    dfa2, states2, transitions2, start_state2, accept_states2 = regex_to_nfa(regex2)
    dfa1 = convert_nfa_to_dfa(dfa1, states1, transitions1, start_state1, accept_states1)
    dfa2 = convert_nfa_to_dfa(dfa2, states2, transitions2, start_state2, accept_states2)
    print(is_isomorphic(dfa1, dfa2))