condition_a = False
condition_b = True

def check_conditions(a, b):
    return a and b

if __name__ == '__main__':
    result = check_conditions(condition_a, condition_b)
    print(result)