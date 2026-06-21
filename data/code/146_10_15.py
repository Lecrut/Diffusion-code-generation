categories = {
    'negative': lambda x: x < 0,
    'zero': lambda x: x == 0,
    'positive': lambda x: x > 0,
    'even': lambda x: x % 2 == 0,
    'odd': lambda x: x % 2 != 0
}

def categorize_number(num):
    for category, condition in categories.items():
        if condition(num):
            return category

if __name__ == '__main__':
    numbers = [-5, 0, 3, 8, 11]
    for number in numbers:
        result = categorize_number(number)
        print(f"Number: {number}, Category: {result}")