class DualStateVerifier:
    def __init__(self, status_a: bool, status_b: bool) -> None:
        self._status_a = bool(status_a)
        self._status_b = bool(status_b)

    def evaluate_negation(self) -> bool:
        return not self._status_a and not self._status_b

    def get_state_pair(self) -> tuple:
        return (self._status_a, self._status_b)

if __name__ == '__main__':
    verifier = DualStateVerifier(False, False)
    print(verifier.evaluate_negation())
    print(verifier.get_state_pair())
    
    verifier_2 = DualStateVerifier(True, False)
    print(verifier_2.evaluate_negation())
    print(verifier_2.get_state_pair())