def check_conditions(first: float, second: float, third: float) -> bool:
    if first <= 0:
        return False
    if second >= first:
        return False
    return third == first + second

if __name__ == '__main__':
    result = check_conditions(10.0, 4.0, 14.0)
    print(result)