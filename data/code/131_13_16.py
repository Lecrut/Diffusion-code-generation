def categorize_string(input_str: str) -> str:
    rules = {
        lambda x: x.startswith('A'): 'Category A',
        lambda x: x.startswith('B'): 'Category B',
        lambda x: x.startswith('C'): 'Category C',
        lambda x: True: 'Default Category'
    }
    
    for rule, category in rules.items():
        if rule(input_str):
            return category

if __name__ == '__main__':
    sample_values = ['Apple', 'Banana', 'Cherry', 'Date']
    for value in sample_values:
        print(f'{value}: {categorize_string(value)}')