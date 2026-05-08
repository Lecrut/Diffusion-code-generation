import re
class BooleanEvaluator:
    def check_precedence(self, expression_string):
        tokens = re.findall(r'\(|\)|\bAND\b|\bOR\b|\bNOT\b|\d+|\+|\-|\(|\)|\,|\s+', expression_string)
        if not tokens:
            return "Error: Empty expression"
        tokens_processed = []
        for token in tokens:
            if token.strip() == "":
                continue
            tokens_processed.append(token)
        if not tokens_processed:
            return "Error: Could not parse expression"
        precedence_map = {
            'NOT': 3,
            'AND': 2,
            'OR': 1,
            '(': 0,
            ')': 0
        }
        evaluation_order = []
        for i, token in enumerate(tokens_processed):
            if token in precedence_map:
                evaluation_order.append((token, precedence_map[token], i))
            else:
                evaluation_order.append((token, 0, i))
        result = []
        for token, prec, index in evaluation_order:
            if token in ('AND', 'OR', 'NOT'):
                result.append({
                    'type': 'operator',
                    'token': token,
                    'precedence': prec,
                    'index': index
                })
            else:
                result.append({
                    'type': 'operand',
                    'token': token,
                    'precedence': 0,
                    'index': index
                })
        return result
if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    test_cases = [
        "A AND B OR C",
        "(A AND B) OR C",
        "NOT A OR B",
        "A AND (B OR C)",
        "A OR B AND C",
        "NOT (A AND B)"
    ]
    for i, expr in enumerate(test_cases):
        print(f"--- Test Case {i+1}: {expr} ---")
        result = evaluator.check_precedence(expr)
        for item in result:
            print(f"Token: {item['token']}, Type: {item['type']}, Precedence: {item['precedence']}, Index: {item['index']}")
        print("-" * 30)
    print("\n--- Complex Scenario Test ---")
    complex_expr = "NOT A AND (B OR NOT C) OR D"
    result = evaluator.check_precedence(complex_expr)
    for item in result:
        print(f"Token: {item['token']}, Type: {item['type']}, Precedence: {item['precedence']}, Index: {item['index']}")
    print("-" * 30)