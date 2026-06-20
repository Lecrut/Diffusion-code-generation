class BooleanNegator:
    @staticmethod
    def negate(value: bool) -> bool:
        return not value

if __name__ == '__main__':
    is_active = True
    print(BooleanNegator.negate(is_active))