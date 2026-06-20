def check_conditions(x):
    return x > 0 and x % 2 == 0 and (x < 100)
if __name__ == '__main__':
    result = check_conditions(42)
    print(result)