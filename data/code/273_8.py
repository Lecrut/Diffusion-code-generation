def repeat_elements(iterable, N):
    return [element for element in iterable for _ in range(N)]
if __name__ == '__main__':
    data = [1, 2, 3]
    n = 3
    result = repeat_elements(data, n)
    print(result)