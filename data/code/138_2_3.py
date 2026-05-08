class BooleanLogic:
    def calculate_table(self):
        P_values = [0, 1]
        Q_values = [0, 1]
        result = []
        for p in P_values:
            for q in Q_values:
                p_and_q = p & q
                result.append((p, q, p_and_q))
        return result
if __name__ == '__main__':
    bl = BooleanLogic()
    table = bl.calculate_table()
    print("P | Q | P AND Q")
    print("---|---|---------")
    for p, q, result in table:
        print(f"{p} | {q} | {result}")