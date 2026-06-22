def get_fibonacci(n: int) -> list:
    if n <= 0:
        return []
    if n == 1:
        return [0]
    result = [0, 1]
    for i in range(2, n):
        a = result[i - 1]
        b = result[i - 2]
        result.append(a + b)
    return result

if __name__ == '__main__':
    terms = get_fibonacci(100)
    for term in terms:
        print(term)