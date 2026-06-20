import sqlparse

def parse_sql_to_ast(sql):
    return sqlparse.parse(sql)[0]

def canonicalize_identifiers(node):
    if isinstance(node, sqlparse.sql.IdentifierList):
        return sqlparse.sql.IdentifierList([canonicalize_identifiers(n) for n in node.get_identifiers()])
    elif isinstance(node, sqlparse.sql.Identifier):
        return sqlparse.sql.Identifier(node.get_real_name())
    else:
        return node

def are_equivalent(sql1, sql2):
    ast1 = canonicalize_identifiers(parse_sql_to_ast(sql1))
    ast2 = canonicalize_identifiers(parse_sql_to_ast(sql2))
    return ast1 == ast2
if __name__ == '__main__':
    sql_query1 = 'SELECT * FROM users WHERE age > 30'
    sql_query2 = 'SELECT * FROM users WHERE age > 30'
    print(are_equivalent(sql_query1, sql_query2))