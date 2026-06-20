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

    def accepts(self, string):
        current_state = self.start_state
        for symbol in string:
            if symbol not in self.alphabet:
                return False
            current_state = self.move(current_state, symbol)
            if current_state is None:
                return False
        return current_state in self.accept_states

def construct_dfa(regex):
    states = set()
    alphabet = set()
    transitions = {}
    start_state = 0
    accept_states = {0}
    for char in regex:
        if char.isalpha():
            alphabet.add(char)
            new_state = len(states)
            states.add(new_state)
            transitions[start_state, char] = new_state
            start_state = new_state
    return DFA(states, alphabet, transitions, 0, accept_states)

def are_equivalent(regex1, regex2):
    dfa1 = construct_dfa(regex1)
    dfa2 = construct_dfa(regex2)

    def is_isomorphic(dfa1, dfa2):
        from collections import deque
        q = deque([(dfa1.start_state, dfa2.start_state)])
        visited = set()
        while q:
            state1, state2 = q.popleft()
            if (state1, state2) in visited:
                continue
            visited.add((state1, state2))
            for char in dfa1.alphabet:
                next_state1 = dfa1.move(state1, char)
                next_state2 = dfa2.move(state2, char)
                if not (next_state1 is None and next_state2 is None):
                    if (state1, state2) != (start_state, start_state):
                        return False
                    q.append((next_state1, next_state2))
        return True
    return is_isomorphic(dfa1, dfa2)
if __name__ == '__main__':
    regex_a = 'ab*'
    regex_b = 'a(b*)'
    print(f"'{regex_a}' and '{regex_b}' are equivalent: {are_equivalent(regex_a, regex_b)}")
    regex_c = '(ab)*'
    regex_d = '(a*b*)*'
    print(f"'{regex_c}' and '{regex_d}' are equivalent: {are_equivalent(regex_c, regex_d)}")