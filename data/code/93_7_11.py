class LogicGate:
    def __init__(self, p_state: bool, q_state: bool):
        if type(p_state) is not bool:
            raise ValueError("p_state must be a boolean")
        if type(q_state) is not bool:
            raise ValueError("q_state must be a boolean")
        self.p_state = p_state
        self.q_state = q_state

    def get_negated_conjunction(self) -> bool:
        return (not self.p_state) and (not self.q_state)

if __name__ == '__main__':
    gate = LogicGate(False, False)
    status = gate.get_negated_conjunction()
    print(status)