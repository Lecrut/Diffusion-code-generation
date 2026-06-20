if __name__ == '__main__':
    sample_inputs = [(False, False), (False, True), (True, False), (True, True)]
    results = [DE_MORGAN_LAWS_VERIFY(A, B) for A, B in sample_inputs]
    print(results)