import re

def regex_to_dfa(regex):
    states = {0}
    transitions = {}
    accepting_states = set()

    def add_transition(state, char, next_state):
        if state not in transitions:
            transitions[state] = {}
        if char not in transitions[state]:
            transitions[state][char] = []
        transitions[state][char].append(next_state)
    stack = [(0, regex)]
    while stack:
        current_state, pattern = stack.pop()
        for match in re.finditer('(\\w|\\(|\\))', pattern):
            char = match.group(1)
            if char == '(':
                new_state = max(states) + 1
                states.add(new_state)
                add_transition(current_state, 'ε', new_state)
                stack.append((new_state, pattern[match.end():]))
            elif char == ')':
                break
            else:
                new_state = max(states) + 1
                states.add(new_state)
                add_transition(current_state, char, new_state)
                accepting_states.add(new_state)
                stack.append((new_state, pattern[match.end():]))
    return (states, transitions, accepting_states)

def dfa_isomorphism(dfa1, dfa2):
    if len(dfa1[0]) != len(dfa2[0]):
        return False
    if len(dfa1[1]) != len(dfa2[1]):
        return False
    if len(dfa1[2]) != len(dfa2[2]):
        return False
    mapping = {}

    def dfs(state1, state2):
        if (state1, state2) in mapping:
            return True
        if state1 not in dfa1[0] or state2 not in dfa2[0]:
            return False
        if set(dfa1[1][state1].values()) != set(dfa2[1][state2].values()):
            return False
        if (state1 in dfa1[2]) != (state2 in dfa2[2]):
            return False
        mapping[state1, state2] = True
        for char in dfa1[1][state1]:
            next_states1 = set(dfa1[1][state1][char])
            next_states2 = set(dfa2[1][state2][char])
            if not all((dfs(next_state1, next_state2) for next_state1, next_state2 in zip(sorted(next_states1), sorted(next_states2)))):
                return False
        return True
    return dfs(0, 0)

def regex_match_same_language(regex1, regex2):
    dfa1 = regex_to_dfa(regex1)
    dfa2 = regex_to_dfa(regex2)
    return dfa_isomorphism(dfa1, dfa2)
if __name__ == '__main__':
    print(regex_match_same_language('a|b', 'b|a'))
    print(regex_match_same_language('(a|b)*', 'c*'))