class BooleanNegator:
    def negate_if_false(self, value):
        return not value

if __name__ == '__main__':
    negator = BooleanNegator()
    print(f"False: {negator.negate_if_false(False)}")
    print(f"True: {negator.negate_if_false(True)}")