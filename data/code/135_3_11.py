import re

def regex_to_dfa(regex):
    states = set()
    alphabet = set()
    transitions = {}
    start_state = 0
    accept_states = set()

    def add_transition(state, symbol, next_state):
        if (state, symbol) not in transitions:
            transitions[state, symbol] = []
        transitions[state, symbol].append(next_state)
    states.add(start_state)
    current_state = start_state
    for char in regex:
        if char == '(' or char == '|':
            continue
        elif char == ')':
            break
        else:
            alphabet.add(char)
            add_transition(current_state, char, current_state + 1)
            states.add(current_state + 1)
            current_state += 1
    return DFA(states, alphabet, transitions, start_state, accept_states)

class DFA:

    def __init__(self, states, alphabet, transitions, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.accept_states = accept_states

    def move(self, state, symbol):
        if (state, symbol) in self.transitions:
            return self.transitions[state, symbol]
        return None

    def accepts(self, word):
        current_state = [self.start_state]
        for symbol in word:
            next_states = set()
            for state in current_state:
                next_states.update(self.move(state, symbol))
            current_state = next_states
        return any((state in self.accept_states for state in current_state))

def are_equivalent(regex1, regex2):
    dfa1 = regex_to_dfa(regex1)
    dfa2 = regex_to_dfa(regex2)
    return dfa1.is_isomorphic(dfa2)

class DFA:

    def __init__(self, states, alphabet, transitions, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.accept_states = accept_states

    def move(self, state, symbol):
        if (state, symbol) in self.transitions:
            return self.transitions[state, symbol]
        return None

    def accepts(self, word):
        current_state = [self.start_state]
        for symbol in word:
            next_states = set()
            for state in current_state:
                next_states.update(self.move(state, symbol))
            current_state = next_states
        return any((state in self.accept_states for state in current_state))

    def is_isomorphic(self, other):
        if len(self.states) != len(other.states) or len(self.alphabet) != len(other.alphabet):
            return False
        state_mapping = {}
        for s1 in self.states:
            found_match = False
            for s2 in other.states:
                if not found_match and set((self.transitions.get((s1, a), []) for a in self.alphabet)) == set((other.transitions.get((s2, a), []) for a in self.alphabet)):
                    state_mapping[s1] = s2
                    found_match = True
            if not found_match:
                return False
        for s1 in self.states:
            if s1 not in state_mapping or any((self.move(s1, a) != state_mapping[self.move(other.state_mapping[s1], a)] for a in self.alphabet)):
                return False
        return True
if __name__ == '__main__':
    regex_a = 'ab|c'
    regex_b = '(a&b)|(c)'
    print(are_equivalent(regex_a, regex_b))