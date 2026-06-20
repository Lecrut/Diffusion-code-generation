from typing import Dict

def categorize_string(input_str: str) -> str:
    rules: Dict[str, lambda x: str] = {'apple': lambda _: 'fruit', 'carrot': lambda _: 'vegetable', 'banana': lambda _: 'fruit', 'spinach': lambda _: 'vegetable'}
    return rules.get(input_str.lower(), lambda _: 'unknown')()
if __name__ == '__main__':
    print(categorize_string('Apple'))
    print(categorize_string('Carrot'))
    print(categorize_string('Banana'))
    print(categorize_string('Spinach'))
    print(categorize_string('Grape'))