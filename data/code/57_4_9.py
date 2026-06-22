def fibonacci():
    a, b = 0, 1
    results = []
    for _ in range(200):
        results.append(a)
        a, b = b, a + b
    return results

if __name__ == '__main__':
    print(fibonacci())