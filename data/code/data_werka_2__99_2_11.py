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
        ast.USub: 4,
        ast.UAdd: 4,
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
        if isinstance(node, ast.Expression):
            return parse_tree(node.body)
        if isinstance(node, ast.Constant):
            return str(node.value)
        if isinstance(node, ast.Name):
            return node.id
        if isinstance(node, ast.BinOp):
            left_str = parse_tree(node.left)
            right_str = parse_tree(node.right)
            op_str = type(node.op).__name__
            prec = get_precedence(node)
            assoc = get_associativity(node)
            
            left_prec = get_precedence(node.left) if isinstance(node.left, (ast.BinOp, ast.UnaryOp)) else 0
            right_prec = get_precedence(node.right) if isinstance(node.right, (ast.BinOp, ast.UnaryOp)) else 0
            
            left_paren = ""
            right_paren = ""
            
            if isinstance(node.left, ast.BinOp):
                if left_prec < prec or (left_prec == prec and assoc == 'left'):
                    left_paren = "("
                elif left_prec == prec and assoc == 'right':
                     if isinstance(node.left.op, ast.Pow) and isinstance(node.op, ast.Pow):
                         left_paren = "("
            
            if isinstance(node.right, ast.BinOp):
                if right_prec < prec or (right_prec == prec and assoc == 'right'):
                    right_paren = ")"
                elif right_prec == prec and assoc == 'left':
                    if isinstance(node.right.op, ast.Pow) and isinstance(node.op, ast.Pow):
                        right_paren = ")"

            return f"{left_paren}{left_str}{right_paren} {op_str} {left_paren}{right_str}{right_paren}"
        
        if isinstance(node, ast.UnaryOp):
            operand_str = parse_tree(node.operand)
            op_str = type(node.op).__name__
            prec = get_precedence(node)
            operand_prec = get_precedence(node.operand) if isinstance(node.operand, (ast.BinOp, ast.UnaryOp)) else 0
            
            paren = ""
            if isinstance(node.operand, ast.BinOp):
                if operand_prec < prec:
                    paren = "("
            
            return f"{op_str}{paren}{operand_str}"
        
        raise ValueError(f"Unsupported node type: {type(node)}")

    results = []
    for expr_str in expressions:
        try:
            tree = ast.parse(expr_str, mode='eval')
            val = eval(compile(tree, '<string>', 'eval'))
            structure = parse_tree(tree)
            results.append({
                'expression': expr_str,
                'value': val,
                'structure': structure
            })
        except Exception as e:
            results.append({
                'expression': expr_str,
                'value': None,
                'structure': f"Error: {str(e)}"
            })
    return results

if __name__ == '__main__':
    exprs = [
        "2 + 3 * 4",
        "(2 + 3) * 4",
        "2 ** 3 ** 2",
        "10 / 2 + 3",
        "10 - 2 * 3"
    ]
    output = evaluate_expressions(exprs)
    for item in output:
        print(f"Expr: {item['expression']}")
        print(f"Value: {item['value']}")
        print(f"Precedence Structure: {item['structure']}")
        print("---")