class MultiplicationTable:
    TABLE_SIZE = 10

    @staticmethod
    def generate(number):
        return {multiplier: number * multiplier for multiplier in range(1, MultiplicationTable.TABLE_SIZE + 1)}

    @staticmethod
    def get_six():
        return MultiplicationTable.generate(6)

if __name__ == '__main__':
    print(MultiplicationTable.get_six())