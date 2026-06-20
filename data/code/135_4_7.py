import sqlparse
from sqlparse.sql import Identifier, IdentifierList

def canonicalize_identifiers(node):
    if isinstance(node, IdentifierList):
        return IdentifierList([canonicalize_identifiers(child) for child in node.get_identifiers()])
    elif isinstance(node, Identifier):
        return Identifier(node.get_real_name())
    else:
        return node

def compare_queries(query1, query2):
    ast1 = sqlparse.parse(query1)[0]
    ast2 = sqlparse.parse(query2)[0]
    canonicalized_ast1 = canonicalize_identifiers(ast1)
    canonicalized_ast2 = canonicalize_identifiers(ast2)
    return canonicalized_ast1 == canonicalized_ast2

if __name__ == '__main__':
    query1 = 'SELECT * FROM users WHERE age > 30'
    query2 = 'select * from Users where Age > 30'
    print(compare_queries(query1, query2))