def are_strictly_true(var1, var2):
    return bool(var1) and bool(var2)
if __name__ == '__main__':
    print(are_strictly_true(True, True))
    print(are_strictly_true(False, True))