if __name__ == '__main__':
    for a in [False, True]:
        for b in [False, True]:
            result = a ^ b
            print(f"a: {a}, b: {b}, a XOR b: {result}")