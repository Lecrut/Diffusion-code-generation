import re
from sqlparse import parse

def canonicalize_identifiers(sql):
    return re.sub('\\b(\\w+)\\b', lambda m: m.group(1).lower(), sql)

def compare_sql_queries(query1, query2):
    parsed_query1 = parse(canonicalize_identifiers(query1))[0]
    parsed_query2 = parse(canonicalize_identifiers(query2))[0]
    return parsed_query1 == parsed_query2
if __name__ == '__main__':
    query1 = 'SELECT * FROM users WHERE age > 30'
    query2 = 'select * from Users where Age > 30'
    print(compare_sql_queries(query1, query2))