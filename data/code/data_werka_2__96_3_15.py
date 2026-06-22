def evaluate_nested_expression(expr):
    OP_MAP = {
        '&': lambda a, b: a and b,
        '|': lambda a, b: a or b,
        '^': lambda a, b: a != b,
        '~': lambda a, b: not a and b,
    }

    def resolve(node):
        if isinstance(node, bool):
            return node
        if isinstance(node, (int, float)):
            return bool(node)
        if not isinstance(node, list) or len(node) == 0:
            raise ValueError("Invalid expression node")
        
        if len(node) == 1:
            return resolve(node[0])
        
        if len(node) == 2:
            left = resolve(node[0])
            right = resolve(node[1])
            if isinstance(left, bool) and isinstance(right, bool):
                return left and right
            raise ValueError("Operands must be boolean")
        
        if len(node) == 3:
            left = resolve(node[0])
            op_symbol = node[1]
            right = resolve(node[2])
            
            if op_symbol not in OP_MAP:
                raise ValueError(f"Unknown operator: {op_symbol}")
            
            return OP_MAP[op_symbol](left, right)
        
        if len(node) == 4:
            left = resolve(node[0])
            op_symbol = node[1]
            mid = resolve(node[2])
            right = resolve(node[3])
            
            if op_symbol not in OP_MAP:
                raise ValueError(f"Unknown operator: {op_symbol}")
            
            first = OP_MAP[op_symbol](left, mid)
            return first and right
        
        raise ValueError(f"Unsupported expression length: {len(node)}")

    return resolve(expr)

if __name__ == '__main__':
    A = True
    B = False
    C = True
    D = False
    
    expr = [
        [
            [
                A,
                '&',
                B
            ],
            '|',
            C
        ],
        '&',
        D
    ]
    
    result = evaluate_nested_expression(expr)
    print(result)