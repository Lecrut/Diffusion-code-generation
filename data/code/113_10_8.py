class MathHelper:
    @staticmethod
    def calculate_difference(a, b):
        return a - b

if __name__ == '__main__':
    difference = MathHelper.calculate_difference(25, 10)
    print(difference)