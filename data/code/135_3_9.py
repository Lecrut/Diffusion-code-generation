import re2 as re

def regex_to_dfa(regex):
    nfa = re.compile(regex).nfa()
    dfa_states = [set()]
    dfa_edges = {}
    visited = set([frozenset(dfa_states[0])])
    while True:
        new_states = set()
        for state in dfa_states:
            for char in 'abcdefghijklmnopqrstuvwxyz':
                next_state = nfa.step(state, char)
                if next_state not in visited:
                    new_states.add(next_state)
                    visited.add(frozenset(next_state))
        if not new_states:
            break
        dfa_states.append(new_states)
    for state in dfa_states:
        if any((nfa.is_accept(s) for s in state)):
            dfa_edges[state] = {}
            for char in 'abcdefghijklmnopqrstuvwxyz':
                next_state = nfa.step(state, char)
                dfa_edges[state][char] = next_state
    return (dfa_states, dfa_edges)

def is_isomorphic(dfa1, dfa2):
    if len(dfa1) != len(dfa2):
        return False
    state_map = {}

    def dfs(state1, state2):
        if (state1, state2) in state_map:
            return True
        if not state1 and (not state2):
            return True
        if not state1 or not state2:
            return False
        for char in 'abcdefghijklmnopqrstuvwxyz':
            next_state1 = dfa1[state1][char]
            next_state2 = dfa2[state2][char]
            if (next_state1, next_state2) not in state_map and (not dfs(next_state1, next_state2)):
                return False
            state_map[state1, state2] = True
        return True
    return dfs(dfa1[0], dfa2[0])

def regex_match_languages(regex1, regex2):
    dfa1, _ = regex_to_dfa(regex1)
    dfa2, _ = regex_to_dfa(regex2)
    return is_isomorphic(dfa1, dfa2)
if __name__ == '__main__':
    print(regex_match_languages('a|b', 'b|a'))
    print(regex_match_languages('a*b', 'b*a'))
    print(regex_match_languages('(a|b)*', '(b|a)*'))
    print(regex_match_languages('a+', 'b+'))