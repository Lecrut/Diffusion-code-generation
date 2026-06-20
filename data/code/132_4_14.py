class Negator:
    def negate_if_false(self, boolean_value):
        return not boolean_value

if __name__ == '__main__':
    negator = Negator()
    print(f"negate_if_false(False): {negator.negate_if_false(False)}")
    print(f"negate_if_false(True): {negator.negate_if_false(True)}")