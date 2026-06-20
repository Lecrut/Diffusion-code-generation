import re2 as re

def regex_to_dfa(regex):
    nfa = re.nfa(regex)
    dfa = re.dfa(nfa)
    return dfa

def is_isomorphic(dfa1, dfa2):
    if len(dfa1.states) != len(dfa2.states):
        return False
    if len(dfa1.alphabet) != len(dfa2.alphabet):
        return False
    for state in dfa1.states:
        if state not in dfa2.states:
            return False
    for symbol in dfa1.alphabet:
        if symbol not in dfa2.alphabet:
            return False
    for state, transitions in dfa1.transitions.items():
        if state not in dfa2.transitions:
            return False
        for symbol, next_state in transitions.items():
            if symbol not in dfa2.transitions[state]:
                return False
            if dfa2.transitions[state][symbol] != next_state:
                return False
    return True

def regex_match_equivalence(regex1, regex2):
    dfa1 = regex_to_dfa(regex1)
    dfa2 = regex_to_dfa(regex2)
    return is_isomorphic(dfa1, dfa2)
if __name__ == '__main__':
    print(regex_match_equivalence('a|b', 'b|a'))
    print(regex_match_equivalence('(a|b)*', '(b|a)*'))
    print(regex_match_equivalence('ab', 'ba'))