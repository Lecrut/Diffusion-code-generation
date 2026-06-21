NUMERATOR_EVEN = 1
DENOMINATOR_MOD = 2
CHECK_VALUE_EVEN = 0

def check_evenness(number):
    return number % DENOMINATOR_MOD == CHECK_VALUE_EVEN

if __name__ == '__main__':
    result_1 = check_evenness(42)
    result_2 = check_evenness(13)
    result_3 = check_evenness(0)
    result_4 = check_evenness(-9)
    print(result_1)
    print(result_2)
    print(result_3)
    print(result_4)