def are_strictly_true(a, b):
    return bool(a) and bool(b)

if __name__ == '__main__':
    condition_x = 1
    condition_y = True
    result = are_strictly_true(condition_x, condition_y)
    print(result)