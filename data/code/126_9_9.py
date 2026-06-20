class ValueComparator:
    VALUE1 = 75
    VALUE2 = 75

    @staticmethod
    def check_equal():
        return ValueComparator.VALUE1 == ValueComparator.VALUE2

if __name__ == '__main__':
    print(ValueComparator.check_equal())