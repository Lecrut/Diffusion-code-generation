if __name__ == '__main__':
    A = 5
    B = 3
    C = 7
    result_and = A & B
    not_C = ~C
    result_or = result_and | not_C
    print(result_or)