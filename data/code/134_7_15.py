class StateVerifier:
    def verify_exclusivity(self, state1: int, state2: int) -> bool:
        return (state1 & ~state2) == 0 and (state2 & ~state1) == 0

if __name__ == '__main__':
    verifier = StateVerifier()
    print(f"Verifying exclusivity of (0, 0): {verifier.verify_exclusivity(0, 0)}")
    print(f"Verifying exclusivity of (0, 1): {verifier.verify_exclusivity(0, 1)}")
    print(f"Verifying exclusivity of (1, 0): {verifier.verify_exclusivity(1, 0)}")
    print(f"Verifying exclusivity of (1, 1): {verifier.verify_exclusivity(1, 1)}")