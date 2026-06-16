def repeat_operation(operation, M):
    return [operation() for _ in range(M)]
if __name__ == '__main__':
    M = 5
    result_list = repeat_operation(lambda: 10, M)
    print(result_list)