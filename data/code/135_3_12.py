import re

def regex_to_dfa(regex):
    states = set()
    alphabet = set()
    transitions = {}
    accept_states = set()

    def add_state(state, char=None):
        if state not in states:
            states.add(state)
            transitions[state] = {}

    def add_transition(from_state, to_state, char):
        if from_state not in transitions:
            transitions[from_state] = {}
        if to_state not in transitions[from_state]:
            transitions[from_state][to_state] = set()
        transitions[from_state][to_state].add(char)
        alphabet.add(char)

    def epsilon_closure(state):
        closure = {state}
        stack = [state]
        while stack:
            current = stack.pop()
            for next_state, chars in transitions.items():
                if current in chars and '' in chars[current]:
                    if next_state not in closure:
                        closure.add(next_state)
                        stack.append(next_state)
        return closure

    def move(closure, char):
        new_closure = set()
        for state in closure:
            if state in transitions and char in transitions[state]:
                new_closure.update(transitions[state][char])
        return epsilon_closure(new_closure)
    add_state('q0')
    current_state = 'q0'
    stack = [current_state]
    while stack:
        current_state = stack.pop()
        for char in alphabet:
            next_states = move(epsilon_closure(current_state), char)
            if next_states not in states:
                add_state(next_state, char)
                add_transition(current_state, next_state, char)
                stack.append(next_state)
    accept_states = {state for state in states if '' in transitions[state]}
    return (states, alphabet, transitions, accept_states)

def dfa_isomorphism(dfa1, dfa2):
    if len(dfa1[0]) != len(dfa2[0]):
        return False
    if len(dfa1[1]) != len(dfa2[1]):
        return False
    if len(dfa1[3]) != len(dfa2[3]):
        return False
    mapping = {}
    stack = list(zip(sorted(dfa1[0]), sorted(dfa2[0])))
    while stack:
        state1, state2 = stack.pop()
        if state1 in mapping and mapping[state1] != state2:
            return False
        if state2 in mapping and mapping[state2] != state1:
            return False
        mapping[state1] = state2
        for char in dfa1[1]:
            next_state1 = dfa1[2][state1].get(char, set())
            next_state2 = dfa2[2][state2].get(char, set())
            if not all((mapping[next_state] == next_state2 for next_state in next_state1)):
                return False
            stack.extend(zip(next_state1, next_state2))
    return True

def regex_match_same_language(regex1, regex2):
    dfa1 = regex_to_dfa(regex1)
    dfa2 = regex_to_dfa(regex2)
    return dfa_isomorphism(dfa1, dfa2)
if __name__ == '__main__':
    print(regex_match_same_language('a|b', 'b|a'))
    print(regex_match_same_language('(a|b)*', 'c*'))