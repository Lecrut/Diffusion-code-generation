import re

def regex_to_dfa(regex):
    nfa = re.compile(regex).pattern
    dfa = {}
    for state in nfa:
        dfa[state] = {}
        for char in set(nfa):
            if char not in dfa[state]:
                dfa[state][char] = []
    return dfa

def is_isomorphic(dfa1, dfa2):
    if len(dfa1) != len(dfa2):
        return False
    for state1 in dfa1:
        if state1 not in dfa2:
            return False
        for char in dfa1[state1]:
            if dfa1[state1][char] != dfa2[state1][char]:
                return False
    return True

def regex_match_same_language(regex1, regex2):
    dfa1 = regex_to_dfa(regex1)
    dfa2 = regex_to_dfa(regex2)
    return is_isomorphic(dfa1, dfa2)
if __name__ == '__main__':
    print(regex_match_same_language('a|b', 'b|a'))
    print(regex_match_same_language('(a|b)*', 'c*'))