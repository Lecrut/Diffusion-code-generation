import re

def parse_sql_to_ast(sql):
    tokens = re.findall('\\b\\w+\\b', sql)
    ast = []
    stack = []
    for token in tokens:
        if token == '(':
            stack.append([])
        elif token == ')':
            sub_ast = stack.pop()
            if stack:
                stack[-1].append(sub_ast)
            else:
                ast = sub_ast
        elif stack:
            stack[-1].append(token)
        else:
            ast.append(token)
    return ast

def canonicalize_identifiers(ast):

    def canonicalize(node):
        if isinstance(node, list):
            return [canonicalize(sub_node) for sub_node in node]
        elif isinstance(node, str) and node.isidentifier():
            return node.lower()
        else:
            return node
    return canonicalize(ast)

def are_equivalent(sql1, sql2):
    ast1 = parse_sql_to_ast(sql1)
    ast2 = parse_sql_to_ast(sql2)
    canon_ast1 = canonicalize_identifiers(ast1)
    canon_ast2 = canonicalize_identifiers(ast2)
    return canon_ast1 == canon_ast2
if __name__ == '__main__':
    sql_query1 = 'SELECT * FROM users WHERE age > 30'
    sql_query2 = 'select * from Users where Age > 30'
    print(are_equivalent(sql_query1, sql_query2))