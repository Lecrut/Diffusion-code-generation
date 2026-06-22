import ast
import operator

def evaluate_expressions(expressions):
    prec_map = {
        ast.Add: 1,
        ast.Sub: 1,
        ast.Mult: 2,
        ast.Div: 2,
        ast.FloorDiv: 2,
        ast.Mod: 2,
        ast.Pow: 3,
        ast.UAdd: 4,
        ast.USub: 4,
        ast.Invert: 4,
    }
    
    def get_precedence(node):
        if isinstance(node, ast.BinOp):
            return prec_map.get(type(node.op), 0)
        if isinstance(node, ast.UnaryOp):
            return prec_map.get(type(node.op), 0)
        return 0

    def get_associativity(node):
        if isinstance(node, ast.BinOp):
            if isinstance(node.op, (ast.Pow,)):
                return 'right'
            return 'left'
        return 'left'

    def parse_tree(node):
        if isinstance(node, ast.Constant):
            return str(node.value)
        if isinstance(node, ast.Name):
            return node.id
        if isinstance(node, ast.BinOp):
            left_str = parse_tree(node.left)
            right_str = parse_tree(node.right)
            op_str = type(node.op).__name__.replace('ast.', '')
            left_prec = get_precedence(node.left)
            right_prec = get_precedence(node.right)
            left_assoc = get_associativity(node.left)
            right_assoc = get_associativity(node.right)
            
            left_paren = left_prec < get_precedence(node) or (left_prec == get_precedence(node) and left_assoc == 'right')
            right_paren = right_prec < get_precedence(node) or (right_prec == get_precedence(node) and right_assoc == 'left')
            
            if isinstance(node.op, ast.Pow) and right_prec == get_precedence(node):
                right_paren = True
                
            left_part = f"({left_str})" if left_paren else left_str
            right_part = f"({right_str})" if right_paren else right_str
            return f"{left_part} {op_str} {right_part}"
        if isinstance(node, ast.UnaryOp):
            op_str = type(node.op).__name__.replace('ast.', '')
            operand_str = parse_tree(node.operand)
            operand_prec = get_precedence(node.operand)
            operand_assoc = get_associativity(node.operand)
            
            need_paren = operand_prec < get_precedence(node) or (operand_prec == get_precedence(node) and operand_assoc == 'right')
            operand_part = f"({operand_str})" if need_paren else operand_str
            return f"{op_str}{operand_part}"
        return str(node)

    results = []
    for expr_str in expressions:
        try:
            tree = ast.parse(expr_str, mode='eval')
            code = compile(tree, '<string>', 'eval')
            val = eval(code)
            structure = parse_tree(tree.body)
            results.append((expr_str, val, structure))
        except Exception as e:
            results.append((expr_str, None, str(e)))
    return results

if __name__ == '__main__':
    exprs = [
        "2 + 3 * 4",
        "(2 + 3) * 4",
        "2 ** 3 ** 2",
        "2 ** (3 ** 2)",
        "10 / 2 + 3",
        "10 / (2 + 3)",
        "-5 + 10",
        "5 * 2 ** 3"
    ]
    output = evaluate_expressions(exprs)
    for expr, val, struct in output:
        print(f"Expr: {expr} | Val: {val} | Structure: {struct}")