def categorize_string(input_str: str) -> str:
    rules = {'apple': lambda x: 'fruit', 'carrot': lambda x: 'vegetable', 'dog': lambda x: 'animal', 'house': lambda x: 'building'}
    return rules.get(input_str, lambda x: 'unknown')(input_str)
if __name__ == '__main__':
    print(categorize_string('apple'))
    print(categorize_string('carrot'))
    print(categorize_string('dog'))
    print(categorize_string('house'))
    print(categorize_string('table'))