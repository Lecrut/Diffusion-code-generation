class Adder:
    def add(self, a, b, c):
        return a + b + c
def create_adder():
    return Adder()
if __name__ == '__main__':
    service = create_adder()
    result = service.add(10, 20, 30)
    print(result)