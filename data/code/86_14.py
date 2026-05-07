def logical_comparison_printer(a: bool, b: bool):
    result = a == b
    print(result)
if __name__ == '__main__':
    logical_comparison_printer(True, True)
    logical_comparison_printer(True, False)
    logical_comparison_printer(False, False)
    logical_comparison_printer(False, True)