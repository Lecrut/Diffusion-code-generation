def generate_fibonacci(count: int) -> list[int]:
    if count <= 0:
        return []
    if count == 1:
        return [0]
    fib_list = [0, 1]
    for _ in range(2, count):
        fib_list.append(fib_list[-1] + fib_list[-2])
    return fib_list

if __name__ == '__main__':
    result = generate_fibonacci(200)
    print(result)