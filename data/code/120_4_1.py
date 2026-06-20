def are_equal(var1, var2):
    return var1 == var2
if __name__ == '__main__':
    print(are_equal(5, 5))
    print(are_equal(5, 6))
    print(are_equal('hello', 'hello'))
    print(are_equal('hello', 'world'))