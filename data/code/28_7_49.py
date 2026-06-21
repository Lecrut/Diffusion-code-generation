def is_larger(a, b):
    COMPARISON_THRESHOLD = 0
    return a > b if a - b > COMPARISON_THRESHOLD else False
if __name__ == '__main__':
    print(is_larger(10, 5))
    print(is_larger(3, 7))
    print(is_larger(-1, -2))
    print(is_larger(0, 0))