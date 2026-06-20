def short_circuit_evaluation():
    a = True
    b = False

    result_and = a and (b or True)
    result_or = not (a and not b)

    return result_and, result_or

if __name__ == '__main__':
    print(short_circuit_evaluation())