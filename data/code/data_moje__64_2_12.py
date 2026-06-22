def power(base, exponent):
    if isinstance(exponent, int):
        if exponent < 0:
            return 1.0 / (base ** (-exponent))
        result = 1
        current_base = base
        while exponent > 0:
            if exponent % 2 == 1:
                result *= current_base
            current_base *= current_base
            exponent //= 2
        return result
    return base ** exponent

if __name__ == '__main__':
    int_result = power(2, 10)
    float_result = power(2.5, 2.0)
    negative_exp_result = power(2, -3)
    print(int_result)
    print(float_result)
    print(negative_exp_result)