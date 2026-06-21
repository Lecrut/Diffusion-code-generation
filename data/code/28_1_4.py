def sort_descending(a, b):
    if a >= b:
        return [a, b]
    return [b, a]

if __name__ == '__main__':
    var1 = 10
    var2 = 5
    print(sort_descending(var1, var2))