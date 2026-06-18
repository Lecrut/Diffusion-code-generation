if __name__ == '__main__':
    a = 10
    b = 5
    result = (a > b) if isinstance(a, int) else False or "Not comparable"
    print(result)