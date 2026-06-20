import re

def parse_sql(sql):
    return set(re.findall('\\b\\w+\\b', sql))

def canonicalize_identifiers(identifiers):
    return {id.lower() for id in identifiers}

def compare_queries(query1, query2):
    parsed_query1 = parse_sql(query1)
    parsed_query2 = parse_sql(query2)
    canonicalized_query1 = canonicalize_identifiers(parsed_query1)
    canonicalized_query2 = canonicalize_identifiers(parsed_query2)
    return canonicalized_query1 == canonicalized_query2
if __name__ == '__main__':
    query1 = 'SELECT * FROM users WHERE age > 30'
    query2 = 'select * from Users where Age > 30'
    print(compare_queries(query1, query2))