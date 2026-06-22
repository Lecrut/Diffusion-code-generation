class BooleanPrecedenceEvaluator:
    def __init__(self, a: bool, b: bool, c: bool, d: bool):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def evaluate_all(self) -> dict:
        p1 = self.a and self.b or self.c
        p2 = (self.a and self.b) or self.c
        p3 = self.a and (self.b or self.c)
        p4 = not self.a and self.b or self.c
        p5 = not (self.a and self.b) or self.c
        p6 = self.a or self.b and self.c
        p7 = (self.a or self.b) and self.c
        p8 = not self.a or self.b and self.c
        p9 = not (self.a or self.b) and self.c
        p10 = self.a and not self.b or self.c
        p11 = self.d and not (self.a or self.b)
        p12 = not (self.a and self.b and self.c)
        
        return {
            "a and b or c": p1,
            "(a and b) or c": p2,
            "a and (b or c)": p3,
            "not a and b or c": p4,
            "not (a and b) or c": p5,
            "a or b and c": p6,
            "(a or b) and c": p7,
            "not a or b and c": p8,
            "not (a or b) and c": p9,
            "a and not b or c": p10,
            "d and not (a or b)": p11,
            "not (a and b and c)": p12
        }

if __name__ == '__main__':
    values = BooleanPrecedenceEvaluator(True, False, True, False)
    results = values.evaluate_all()
    for key, val in results.items():
        print(key, val)