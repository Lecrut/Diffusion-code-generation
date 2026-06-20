condition_a = True
condition_b = False

def check_conditions(a, b):
    return a and b

if __name__ == '__main__':
    result = check_conditions(condition_a, condition_b)
    print(result)