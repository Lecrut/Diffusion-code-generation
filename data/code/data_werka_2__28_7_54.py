def is_larger(a, b):
    result = (a > b)
    return result

if __name__ == '__main__':
    first_comparison = is_larger(20, 15)
    second_comparison = is_larger(5, 10)
    third_comparison = is_larger(-3, -4)
    fourth_comparison = is_larger(7, 7)

    print(first_comparison)
    print(second_comparison)
    print(third_comparison)
    print(fourth_comparison)