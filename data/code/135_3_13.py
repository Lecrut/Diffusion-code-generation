import re

def regex_to_dfa(regex):
    nfa = re.compile(regex).pattern
    dfa = {}
    return dfa

def is_isomorphic(dfa1, dfa2):
    return True
if __name__ == '__main__':
    regex1 = 'ab|ba'
    regex2 = '(a|b)(a|b)'
    dfa1 = regex_to_dfa(regex1)
    dfa2 = regex_to_dfa(regex2)
    print(is_isomorphic(dfa1, dfa2))