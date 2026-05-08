class BooleanEvaluator:
    def check_complex_condition(self, a: bool, b: bool, c: bool, d: bool) -> bool:
        result = (a and b) or (c and not d)
        return result
if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    a1, b1, c1, d1 = True, True, True, False
    result1 = evaluator.check_complex_condition(a1, b1, c1, d1)
    print(f"a={a1}, b={b1}, c={c1}, d={d1} -> Result: {result1}")
    a2, b2, c2, d2 = True, False, False, True
    result2 = evaluator.check_complex_condition(a2, b2, c2, d2)
    print(f"a={a2}, b={b2}, c={c2}, d={d2} -> Result: {result2}")
    a3, b3, c3, d3 = False, False, True, False
    result3 = evaluator.check_complex_condition(a3, b3, c3, d3)
    print(f"a={a3}, b={b3}, c={c3}, d={d3} -> Result: {result3}")
    a4, b4, c4, d4 = True, True, False, True
    result4 = evaluator.check_complex_condition(a4, b4, c4, d4)
    print(f"a={a4}, b={b4}, c={c4}, d={d4} -> Result: {result4}")