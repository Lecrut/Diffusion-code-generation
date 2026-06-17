def repeat_operation(operation, M):
    return [operation(i) for i in range(M)]
if __name__ == '__main__':
    M = 5
    result_list = repeat_operation(lambda x: x * 2, M)
    print(result_list)