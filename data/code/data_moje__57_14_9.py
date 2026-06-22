def fibonacci_dynamic(n):
    if n <= 0:
        return []
    return [0 if i == 0 else 1 if i == 1 else sum([fibonacci_dynamic(i)[-1], fibonacci_dynamic(i)[-2]]) for i in range(n)]

if __name__ == '__main__':
    print(fibonacci_dynamic(15))