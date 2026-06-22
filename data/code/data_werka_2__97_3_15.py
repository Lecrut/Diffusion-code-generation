class ImplicationTruthTable:
    ROWS = []
    HEADER = "P\tQ\tP -> Q"
    
    @staticmethod
    def compute(p: bool, q: bool) -> bool:
        return (not p) or q
    
    @classmethod
    def generate(cls):
        values = [False, True]
        results = []
        for p in values:
            for q in values:
                r = cls.compute(p, q)
                results.append((p, q, r))
        return results
    
    @staticmethod
    def format_row(p: bool, q: bool, r: bool) -> str:
        return f"P={str(p):<5}Q={str(q):<5}P -> Q={str(r)}"

if __name__ == '__main__':
    table_data = ImplicationTruthTable.generate()
    print(ImplicationTruthTable.HEADER)
    for p, q, r in table_data:
        print(ImplicationTruthTable.format_row(p, q, r))