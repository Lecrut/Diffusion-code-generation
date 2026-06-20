import numpy as np

class LogicalGates:
    @staticmethod
    def and_gate(a: np.ndarray, b: np.ndarray) -> np.ndarray:
        return np.logical_and(a, b)

    @staticmethod
    def or_gate(a: np.ndarray, b: np.ndarray) -> np.ndarray:
        return np.logical_or(a, b)

    @staticmethod
    def not_gate(a: np.ndarray) -> np.ndarray:
        return np.logical_not(a)

if __name__ == '__main__':
    a = np.array([True, False, True, False])
    b = np.array([False, False, True, True])

    and_result = LogicalGates.and_gate(a, b)
    or_result = LogicalGates.or_gate(a, b)
    not_a_result = LogicalGates.not_gate(a)

    print("AND:", and_result)
    print("OR:", or_result)
    print("NOT A:", not_a_result)