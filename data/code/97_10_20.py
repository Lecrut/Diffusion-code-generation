class LogicalExpressionEvaluator:
    def __init__(self, expression_str):
        if not isinstance(expression_str, str) or len(expression_str.strip()) == 0:
            raise ValueError("Expression must be a non-empty string")
        self.expression_str = expression_str.strip()
        self.variables = self._parse_variables()
        if len(self.variables) != 2:
            raise ValueError("Expression must involve exactly two variables")
        self.var_list = sorted(self.variables)

    def _parse_variables(self):
        vars_found = set()
        for char in self.expression_str:
            if char.isalpha():
                vars_found.add(char.lower())
        return vars_found

    def _evaluate_expression(self, p_val, q_val):
        local_vars = {
            self.var_list[0]: p_val,
            self.var_list[1]: q_val
        }
        expr = self.expression_str.lower()
        expr = expr.replace('and', ' and ')
        expr = expr.replace('or', ' or ')
        expr = expr.replace('not', ' not ')
        expr = expr.replace(' xor ', ' ^ ')
        try:
            result = eval(expr, {"__builtins__": {}}, local_vars)
            if not isinstance(result, bool):
                result = bool(result)
            return result
        except Exception as e:
            raise ValueError(f"Error evaluating expression: {e}")

    def generate_table(self):
        rows = []
        for p in [False, True]:
            for q in [False, True]:
                res = self._evaluate_expression(p, q)
                rows.append((p, q, res))
        return rows

    def display_table(self):
        rows = self.generate_table()
        var1, var2 = self.var_list
        header = f"{var1.upper():<6} {var2.upper():<6} Result"
        separator = "-" * len(header)
        print(header)
        print(separator)
        for p, q, res in rows:
            row_str = f"{str(p):<6} {str(q):<6} {str(res):<6}"
            print(row_str)

def evaluate_and(p, q):
    return p and q

def evaluate_or(p, q):
    return p or q

def evaluate_nand(p, q):
    return not (p and q)

if __name__ == '__main__':
    expr1 = LogicalExpressionEvaluator("p and q")
    expr1.display_table()
    print()
    expr2 = LogicalExpressionEvaluator("p or q")
    expr2.display_table()
    print()
    expr3 = LogicalExpressionEvaluator("not (p and q)")
    expr3.display_table()