class DollarConverter:
    FACTOR = 100
    @staticmethod
    def to_cents(dollars):
        return int(dollars * DollarConverter.FACTOR)

if __name__ == '__main__':
    print(DollarConverter.to_cents(42.85))
    print(DollarConverter.to_cents(0.10))