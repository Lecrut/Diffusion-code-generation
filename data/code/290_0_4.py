def kg_to_pounds(kg):
    if not isinstance(kg, (int, float)):
        raise ValueError('Input must be a number')
    return kg * 2.20462
if __name__ == '__main__':
    try:
        print(kg_to_pounds(1))
        print(kg_to_pounds(5))
        print(kg_to_pounds(10))
        print(kg_to_pounds('a'))
    except ValueError as e:
        print(e)