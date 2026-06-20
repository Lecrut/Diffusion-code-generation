import sqlparse
from sqlparse.sql import IdentifierList, Identifier, Where

def parse_sql_to_ast(sql_query):
    return sqlparse.parse(sql_query)[0]

def canonicalize_identifiers(node):
    if isinstance(node, IdentifierList):
        return IdentifierList([canonicalize_identifiers(child) for child in node.get_identifiers()])
    elif isinstance(node, Identifier):
        return Identifier(node.get_real_name())
    elif isinstance(node, Where):
        condition = node.tokens[1]
        canonicalized_condition = canonicalize_expression(condition)
        return Where(canonicalized_condition)
    else:
        return node

def canonicalize_expression(expression):
    new_tokens = []
    for token in expression.tokens:
        if isinstance(token, Identifier):
            new_tokens.append(Identifier(token.get_real_name()))
        elif isinstance(token, sqlparse.sql.Parenthesis):
            new_tokens.append(Parenthesis(canonicalize_expression(token)))
        else:
            new_tokens.append(token)
    return expression.copy(tokens=new_tokens)

def compare_sql_queries(query1, query2):
    ast1 = parse_sql_to_ast(query1)
    ast2 = parse_sql_to_ast(query2)
    canonicalized_ast1 = canonicalize_identifiers(ast1)
    canonicalized_ast2 = canonicalize_identifiers(ast2)
    return canonicalized_ast1 == canonicalized_ast2

if __name__ == '__main__':
    query1 = 'SELECT * FROM users WHERE age > 30'
    query2 = 'select * from Users where Age > 30'
    print(compare_sql_queries(query1, query2))