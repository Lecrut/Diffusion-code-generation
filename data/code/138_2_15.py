import itertools

def truth_table(operator):
    operators = {
        'AND': lambda x, y: x and y,
        'OR': lambda x, y: x or y,
        'NOT': lambda x: not x,
        'XOR': lambda x, y: x != y,
        'NOR': lambda x, y: not (x or y),
        'NAND': lambda x, y: not (x and y)
    }
    
    if operator in operators:
        table = list(itertools.product([False, True], repeat=2))
        print(f"Truth Table for {operator}:")
        for row in table:
            result = operators[operator](*row) if operator != 'NOT' else operators[operator](row[0])
            print(f"{row[0]} {operator} {row[1]} = {result}")
    else:
        print("Invalid operator")

if __name__ == '__main__':
    truth_table('AND')
    truth_table('OR')
    truth_table('NOT')
    truth_table('XOR')
    truth_table('NOR')
    truth_table('NAND')