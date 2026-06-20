def divide_lists(dividends, divisors):
    if len(dividends) != len(divisors):
        raise ValueError('Lists must be of equal length')
    quotient_list = []
    for dividend, divisor in zip(dividends, divisors):
        if divisor == 0:
            quotient_list.append(None)
        else:
            quotient_list.append(dividend / divisor)
    return quotient_list
if __name__ == '__main__':
    list1 = [20, 30, 40, 50]
    list2 = [2, 3, 0, 5]
    result = divide_lists(list1, list2)
    print(result)