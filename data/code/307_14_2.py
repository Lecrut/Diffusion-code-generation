def repeat_operation(M: int, operation: callable, initial_value: any) -> list:
    return [operation(initial_value) for _ in range(M)]
if __name__ == '__main__':
    M = 5
    operation = lambda x: x * 2
    initial_value = 1
    result_list = repeat_operation(M, operation, initial_value)
    print(result_list)