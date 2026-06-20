def short_circuit_demo():
    a = True
    b = False
    print(a or b)
    print(b and a)
    print(not a)
    print(not b)
if __name__ == '__main__':
    short_circuit_demo()