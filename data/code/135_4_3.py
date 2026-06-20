import re

def parse_sql_to_ast(sql):
    tokens = re.findall('\\b\\w+\\b', sql)
    return tokens

def canonicalize_identifiers(tokens):
    return ['IDENTIFIER' if token.isalpha() else token for token in tokens]

def compare_sql_queries(query1, query2):
    ast1 = parse_sql_to_ast(query1)
    ast2 = parse_sql_to_ast(query2)
    canonicalized1 = canonicalize_identifiers(ast1)
    canonicalized2 = canonicalize_identifiers(ast2)
    return canonicalized1 == canonicalized2
if __name__ == '__main__':
    query1 = 'SELECT * FROM users WHERE age > 30'
    query2 = 'SELECT * FROM users WHERE age > 30'
    print(compare_sql_queries(query1, query2))