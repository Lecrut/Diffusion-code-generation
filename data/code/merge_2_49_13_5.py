def is_strictly_positive(value: float) -> bool:
    return value > 0
if __name__ == '__main__':
    result = is_strictly_positive(5.2)
    print(result)
    neg_result = is_strictly_positive(-3.14)
    print(neg_result)