import re

def regex_to_dfa(regex):
    nfa = re.compile(regex).scanner('').match().groupdict()
    dfa_states = [set()]
    dfa_transitions = {}
    visited_states = set()
    while True:
        state = dfa_states[-1]
        if state not in visited_states:
            visited_states.add(state)
            for char in set(''.join(nfa.keys())):
                next_state = {nfa[next_char] for next_char in nfa if any((char in s for s in state))}
                if next_state and next_state not in dfa_states:
                    dfa_states.append(next_state)
                dfa_transitions[state, char] = next_state
    return (dfa_states, dfa_transitions)

def is_isomorphic(dfa1, dfa2):
    if len(dfa1[0]) != len(dfa2[0]):
        return False
    state_mapping = {}

    def dfs(state1, state2):
        if (state1, state2) in state_mapping:
            return True
        if state1 not in dfa1[0] or state2 not in dfa2[0]:
            return False
        state_mapping[state1, state2] = True
        for char in set(''.join(dfa1[1].keys())):
            next_state1 = dfa1[1][state1, char]
            next_state2 = dfa2[1][state2, char]
            if not dfs(next_state1, next_state2):
                return False
        return True
    return dfs(dfa1[0][0], dfa2[0][0])

def regex_match_languages(regex1, regex2):
    dfa1 = regex_to_dfa(regex1)
    dfa2 = regex_to_dfa(regex2)
    return is_isomorphic(dfa1, dfa2)
if __name__ == '__main__':
    print(regex_match_languages('a|b', 'b|a'))
    print(regex_match_languages('(a|b)*', 'c*'))