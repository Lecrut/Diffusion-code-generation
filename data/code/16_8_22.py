def is_positive(number):
    return number > 0
if __name__ == '__main__':
    try:
        user_input = int('42')
        result = is_positive(user_input)
        print(result)
    except ValueError:
        print(False)