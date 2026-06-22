class IntegerComparator:
    GREATER = 1
    LESS_OR_EQUAL = 0

    @staticmethod
    def determine_relationship(x, y):
        if not isinstance(x, int) or not isinstance(y, int):
            raise ValueError("Inputs must be integers")
        return x > y

if __name__ == '__main__':
    val_x = 7
    val_y = 4
    result = IntegerComparator.determine_relationship(val_x, val_y)
    print(result)