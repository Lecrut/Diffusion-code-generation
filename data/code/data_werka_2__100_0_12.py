def check_sign(n):
    if n == 0:
        return "zero"
    return "positive" if n > 0 else "negative"

if __name__ == '__main__':
    values = [8, -12, 0, 0.001, -0.001]
    for v in values:
        result = check_sign(v)
        print(result)