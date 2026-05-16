class BooleanLogic:
    def calculate_table(self):
        P_values = [0, 1]
        Q_values = [0, 1]
        results = []
        for p in P_values:
            for q in Q_values:
                p_and_q = p & q
                results.append((p, q, p_and_q))
        print("P | Q | P AND Q")
        print("---|---|---------")
        for p, q, result in results:
            print(f"{p} | {q} | {result}")
if __name__ == '__main__':
    logic = BooleanLogic()
    logic.calculate_table()