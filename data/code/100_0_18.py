number_categories = {
    'positive': lambda num: num > 0,
    'negative': lambda num: num < 0,
    'zero': lambda num: num == 0
}

def check_number(num):
    for category, condition in number_categories.items():
        if condition(num):
            return category

if __name__ == '__main__':
    print(check_number(5))
    print(check_number(-3))
    print(check_number(0))