EVEN_CHECK_MASK = 1

def check_condition(n):
    return n > 0 and n & EVEN_CHECK_MASK == 0
if __name__ == '__main__':
    print(check_condition(4))
    print(check_condition(-2))
    print(check_condition(0))
    print(check_condition(3))