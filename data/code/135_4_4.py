import sqlparse

def parse_sql_to_ast(sql_query):
    return sqlparse.parse(sql_query)[0]

def canonicalize_identifiers(node):
    if isinstance(node, sqlparse.sql.IdentifierList):
        return sqlparse.sql.IdentifierList([canonicalize_identifiers(child) for child in node.get_identifiers()])
    elif isinstance(node, sqlparse.sql.Identifier):
        return sqlparse.sql.Identifier(node.get_real_name())
    else:
        return node

def are_queries_equivalent(query1, query2):
    ast1 = parse_sql_to_ast(query1)
    ast2 = parse_sql_to_ast(query2)
    canonicalized_ast1 = canonicalize_identifiers(ast1)
    canonicalized_ast2 = canonicalize_identifiers(ast2)
    return canonicalized_ast1 == canonicalized_ast2
if __name__ == '__main__':
    query1 = 'SELECT * FROM users WHERE age > 30'
    query2 = 'SELECT * FROM users WHERE 30 < age'
    print(are_queries_equivalent(query1, query2))