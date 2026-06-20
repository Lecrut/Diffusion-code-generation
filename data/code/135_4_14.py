import sqlparse
from sqlparse.sql import IdentifierList, Identifier

def parse_sql_to_ast(sql_query):
    return sqlparse.parse(sql_query)[0]

def canonicalize_identifiers(node):
    if isinstance(node, IdentifierList):
        return IdentifierList([canonicalize_identifiers(child) for child in node.get_identifiers()])
    elif isinstance(node, Identifier):
        return Identifier(node.get_real_name())
    else:
        return node

def compare_queries(query1, query2):
    ast1 = parse_sql_to_ast(query1)
    ast2 = parse_sql_to_ast(query2)
    canonicalized_ast1 = canonicalize_identifiers(ast1)
    canonicalized_ast2 = canonicalize_identifiers(ast2)
    return canonicalized_ast1 == canonicalized_ast2

def validate_queries(query1, query2):
    if not isinstance(query1, str) or not isinstance(query2, str):
        raise ValueError("Both queries must be strings.")
    if len(query1.strip()) == 0 or len(query2.strip()) == 0:
        raise ValueError("Queries cannot be empty.")

if __name__ == '__main__':
    query1 = 'SELECT * FROM users WHERE age > 30'
    query2 = 'select * from Users where Age > 30'
    
    validate_queries(query1, query2)
    print(compare_queries(query1, query2))