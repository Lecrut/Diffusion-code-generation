class MultiplicationTable:
    TARGET_NUMBER = 4

    @staticmethod
    def generate() -> list[str]:
        return [f"{MultiplicationTable.TARGET_NUMBER} x {i} = {MultiplicationTable.TARGET_NUMBER * i}" for i in range(1, 11)]

    @staticmethod
    def display() -> None:
        for entry in MultiplicationTable.generate():
            print(entry)

if __name__ == '__main__':
    MultiplicationTable.display()