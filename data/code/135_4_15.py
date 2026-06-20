import sqlparse

def parse_sql(query):
    return sqlparse.parse(query)[0]

def canonicalize_identifiers(node):
    if isinstance(node, sqlparse.sql.IdentifierList):
        return sqlparse.sql.IdentifierList([canonicalize_identifiers(n) for n in node.get_identifiers()])
    elif isinstance(node, sqlparse.sql.Identifier):
        return sqlparse.sql.Identifier(node.get_real_name())
    else:
        return node

def are_equivalent(query1, query2):
    parsed1 = parse_sql(query1)
    parsed2 = parse_sql(query2)
    canonicalized1 = canonicalize_identifiers(parsed1)
    canonicalized2 = canonicalize_identifiers(parsed2)
    return canonicalized1 == canonicalized2
if __name__ == '__main__':
    query1 = 'SELECT * FROM users WHERE age > 30'
    query2 = 'SELECT * FROM users WHERE age > 30'
    print(are_equivalent(query1, query2))