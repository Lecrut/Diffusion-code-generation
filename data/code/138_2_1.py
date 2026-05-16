class BooleanLogic:
    def calculate_table(self):
        P_values = [0, 1]
        Q_values = [0, 1]
        results = []
        operation = lambda p, q: p and q
        for p in P_values:
            for q in Q_values:
                result = operation(p, q)
                results.append((p, q, result))
        return results
if __name__ == '__main__':
    bl = BooleanLogic()
    table = bl.calculate_table()
    print("P | Q | P AND Q")
    for p, q, result in table:
        print(f"{p} | {q} | {result}")