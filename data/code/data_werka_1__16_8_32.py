def is_positive(number):
    return number > 0

def main():
    try:
        user_input = '42'
        user_value = int(user_input)
        result = is_positive(user_value)
        print(result)
    except ValueError:
        print('False')
if __name__ == '__main__':
    main()