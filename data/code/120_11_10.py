def compare_variables(var1, var2):
    return var1 == var2
if __name__ == '__main__':
    result = compare_variables(5, 5)
    print(result)
    result = compare_variables(5, '5')
    print(result)
    result = compare_variables([1, 2], [1, 2])
    print(result)
    result = compare_variables([1, 2], (1, 2))
    print(result)