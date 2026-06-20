def check_equality(var1, var2):
    return var1 == var2
if __name__ == '__main__':
    print(check_equality(5, 5))
    print(check_equality(5, 6))
    print(check_equality('hello', 'hello'))
    print(check_equality('hello', 'world'))