class TruthTable:
    @staticmethod
    def implication(p: bool, q: bool) -> bool:
        return not p or q

if __name__ == '__main__':
    for A in (False, True):
        for B in (False, True):
            print(f"A: {A}, B: {B}, A implies B: {TruthTable.implication(A, B)}")