def sum_numeric(*args) -> float:
    return sum(args)
if __name__ == '__main__':
    result = sum_numeric(10, 20.5, -3)
    print(result)