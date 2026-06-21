class TruthTableSolver:

    def evaluate(self, P: bool, Q: bool, expression: str) -> bool:
        table = {('P', 'Q'): lambda p, q: p and q, ('P', '!Q'): lambda p, q: p and (not q), ('!P', 'Q'): lambda p, q: not p and q, ('!P', '!Q'): lambda p, q: not p and (not q), ('P', 'Q|Q'): lambda p, q: p and (q or q), ('P|Q', 'Q'): lambda p, q: (p or q) and q}
        key = (tuple('P' if P else '!P'), tuple('Q' if Q else '!Q'))
        operation = table.get(key, lambda _, __: False)
        return operation(P, Q)
if __name__ == '__main__':
    solver = TruthTableSolver()
    result1 = solver.evaluate(True, True, ('P', 'Q'))
    print(result1)
    result2 = solver.evaluate(False, True, ('!P', 'Q'))
    print(result2)