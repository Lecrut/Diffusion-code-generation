CONDITION_A = True
CONDITION_B = False

def check_conditions(a=CONDITION_A, b=CONDITION_B):
    return a and b

if __name__ == '__main__':
    result = check_conditions()
    print(result)