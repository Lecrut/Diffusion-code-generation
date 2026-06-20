import re

def regex_to_dfa(regex):
    nfa = re.compile(regex).to_nfa()
    dfa = nfa.minimize()
    return dfa

def are_languages_equivalent(regex1, regex2):
    dfa1 = regex_to_dfa(regex1)
    dfa2 = regex_to_dfa(regex2)
    return dfa1.is_isomorphic(dfa2)
if __name__ == '__main__':
    print(are_languages_equivalent('a|b', 'b|a'))
    print(are_languages_equivalent('(a|b)*', 'c*'))