def check_equivalence(stmt1, stmt2):
    values = [0, 1, -1, 2, -2, 3.5, -3.5]
    for value in values:
        if eval(stmt1) != eval(stmt2):
            return False
    return True

if __name__ == '__main__':
    print(check_equivalence('x**2', 'x*x'))