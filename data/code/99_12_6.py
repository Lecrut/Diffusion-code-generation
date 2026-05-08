import re
class BooleanEvaluator:
    def check_precedence(self, expression_string):
        tokens = re.findall(r'\(|\)|\+|\-|\*|\/|\btrue\b|\bfalse\b|\bAND\b|\bOR\b|\bNOT\b|\b\d+\.\d+|\d+', expression_string.replace(' ', ''))
        if not tokens:
            return "Error: Empty expression"
        precedence_map = {
            'NOT': 3,
            'AND': 2,
            'OR': 1,
            '(': 0,
            ')': 0
        }
        output_queue = []
        operator_stack = []
        precedence = {'NOT': 3, 'AND': 2, 'OR': 1}
        for token in tokens:
            if token in ('true', 'false'):
                output_queue.append(token)
            elif token == '(':
                operator_stack.append(token)
            elif token == ')':
                while operator_stack and operator_stack[-1] != '(':
                    output_queue.append(operator_stack.pop())
                if operator_stack and operator_stack[-1] == '(':
                    operator_stack.pop()
            elif token in precedence:
                while (operator_stack and operator_stack[-1] != '(' and 
                       precedence.get(operator_stack[-1], 0) >= precedence[token]):
                    output_queue.append(operator_stack.pop())
                operator_stack.append(token)
            else:
                if token in ('AND', 'OR'):
                    operator_stack.append(token)
        while operator_stack:
            output_queue.append(operator_stack.pop())
        return "Evaluation Order Simulated: " + " -> ".join(output_queue)
if __name__ == '__main__':
    evaluator = BooleanEvaluator()
    expr1 = "true OR false AND true"
    result1 = evaluator.check_precedence(expr1)
    print(f"Expression: {expr1}")
    print(f"Result: {result1}\n")
    expr2 = "(true OR false) AND true"
    result2 = evaluator.check_precedence(expr2)
    print(f"Expression: {expr2}")
    print(f"Result: {result2}\n")
    expr3 = "NOT true AND (false OR NOT false)"
    result3 = evaluator.check_precedence(expr3)
    print(f"Expression: {expr3}")
    print(f"Result: {result3}\n")
    expr4 = "true OR false OR true AND false"
    result4 = evaluator.check_precedence(expr4)
    print(f"Expression: {expr4}")
    print(f"Result: {result4}\n")
    expr5 = "NOT (true AND false) OR (true OR false)"
    result5 = evaluator.check_precedence(expr5)
    print(f"Expression: {expr5}")
    print(f"Result: {result5}\n")