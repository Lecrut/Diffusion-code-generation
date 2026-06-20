def short_circuit_evaluation():
    a = True
    b = False
    result_and = a and 1 / 0
    print(result_and)
    result_or = b or 1 / 0
    print(result_or)
if __name__ == '__main__':
    try:
        short_circuit_evaluation()
    except Exception as e:
        print(e)