def repeat_operation(operation, m):
    return [operation() for _ in range(m)]
if __name__ == '__main__':
    M = 5
    result_list = repeat_operation(lambda: 10, M)
    print(result_list)