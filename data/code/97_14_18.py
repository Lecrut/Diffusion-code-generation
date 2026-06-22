class OrTruthTable:
    INPUTS = [True, False]

    @staticmethod
    def _compute_row(p, q):
        return {"p": p, "q": q, "p | q": p or q}

    @classmethod
    def generate(cls):
        table = []
        for p in cls.INPUTS:
            for q in cls.INPUTS:
                table.append(cls._compute_row(p, q))
        return table

if __name__ == '__main__':
    result = OrTruthTable.generate()
    print(result)