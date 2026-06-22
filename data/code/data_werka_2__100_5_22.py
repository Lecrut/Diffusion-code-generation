def check_logic_consistency(a, b):
    expected = a and b
    return expected

if __name__ == '__main__':
    result = check_logic_consistency(True, False)
    print(result)