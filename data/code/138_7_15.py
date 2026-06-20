class XORTabulator:
    XOR_TABLE = [(False, False, False), (False, True, True), (True, False, True), (True, True, False)]

    @staticmethod
    def xor_generator():
        for p, q, _ in XORTabulator.XOR_TABLE:
            yield (p, q)

if __name__ == '__main__':
    tabulator = XORTabulator()
    for p, q in tabulator.xor_generator():
        print(f"P: {p}, Q: {q}")