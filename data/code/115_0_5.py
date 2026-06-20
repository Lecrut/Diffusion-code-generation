def safe_divide(num, denom):
    if denom == 0:
        return None
    return num / denom
if __name__ == '__main__':
    result = safe_divide(10, 2)
    print(result)
    result = safe_divide(5, 0)
    print(result)