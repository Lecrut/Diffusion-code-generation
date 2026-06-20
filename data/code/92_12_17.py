class BooleanOpposite:
    TRUE = 'True'
    FALSE = 'False'

    @staticmethod
    def get_opposite(value):
        if value.lower() == BooleanOpposite.TRUE.lower():
            return BooleanOpposite.FALSE
        elif value.lower() == BooleanOpposite.FALSE.lower():
            return BooleanOpposite.TRUE
        else:
            raise ValueError("Invalid boolean value")

if __name__ == '__main__':
    manipulator = BooleanOpposite()
    sample1 = 'True'
    opposite1 = manipulator.get_opposite(sample1)
    print(f"Original: {sample1}, Opposite: {opposite1}")
    sample2 = 'false'
    opposite2 = manipulator.get_opposite(sample2)
    print(f"Original: {sample2}, Opposite: {opposite2}")