def verify_status(a: bool, b: bool) -> bool:
    return a ^ b

if __name__ == '__main__':
    val1 = True
    val2 = False
    result1 = verify_status(val1, val2)
    print(result1)

    val3 = False
    val4 = True
    result2 = verify_status(val3, val4)
    print(result2)