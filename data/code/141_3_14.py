import numpy as np

class LogicalGates:
    def and_gate(self, A, B):
        return np.logical_and(A, B)

    def or_gate(self, A, B):
        return np.logical_or(A, B)

    def not_gate(self, A):
        return np.logical_not(A)

if __name__ == '__main__':
    gate_instance = LogicalGates()
    a = np.array([True, False, True, False])
    b = np.array([False, False, True, True])
    print("AND:", gate_instance.and_gate(a, b))
    print("OR:", gate_instance.or_gate(a, b))
    print("NOT A:", gate_instance.not_gate(a))