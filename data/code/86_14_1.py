def compare_and_print(a, b):
    result = a == b
    print(result)
if __name__ == '__main__':
    compare_and_print(True, True)
    compare_and_print(True, False)
    compare_and_print(False, False)
    compare_and_print(True, False)