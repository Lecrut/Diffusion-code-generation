class BooleanInverter:
    @staticmethod
    def invert(value: bool) -> bool:
        return not value

if __name__ == '__main__':
    test_value = True
    result = BooleanInverter.invert(test_value)
    print(result)