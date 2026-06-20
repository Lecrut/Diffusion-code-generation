from sqlparse import parse, tokens

def canonicalize_identifiers(sql):
    parsed = parse(sql)
    for token in parsed.tokens:
        if isinstance(token, tokens.Keyword) or isinstance(token, tokens.Name):
            token.value = token.value.lower()
    return str(parsed)

def compare_queries(query1, query2):
    return canonicalize_identifiers(query1) == canonicalize_identifiers(query2)
if __name__ == '__main__':
    query1 = 'SELECT * FROM users WHERE age > 30'
    query2 = 'select * from Users where Age > 30'
    print(compare_queries(query1, query2))