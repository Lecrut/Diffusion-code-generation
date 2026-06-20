class SimpleAdder:
    def add(self, a, b):
        return int(a) + int(b)

if __name__ == '__main__':
    adder = SimpleAdder()
    print(adder.add(5, 10))
    print(adder.add("5", "10"))