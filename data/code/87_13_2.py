def check_conditions(a, b):
    return (a and not b) or (not a and b)

if __name__ == '__main__':
    result = check_conditions(True, False)
    print(result)