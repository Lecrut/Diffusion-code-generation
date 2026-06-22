class BooleanNegator:
    def __init__(self, value):
        if not isinstance(value, bool):
            raise ValueError("Input must be a boolean")
        self.value = value

    def get_original(self):
        return self.value

    def get_negated(self):
        return not self.value

    def __str__(self):
        return f"Original: {self.value}, Negated: {self.get_negated()}"

if __name__ == '__main__':
    test_cases = [True, False]
    for val in test_cases:
        negator = BooleanNegator(val)
        print(negator.get_negated())
        print(negator)
        print(negator.get_original())
        print("---")
        if val == False:
            break
        val = not val
        negator2 = BooleanNegator(val)
        print(negator2.get_negated())
        print(negator2)
        print(negator2.get_original())
        print("---")
        break
    final_val = True
    negator_final = BooleanNegator(final_val)
    print(negator_final.get_negated())
    print(negator_final)
    print(negator_final.get_original())
    print("---")
    final_val2 = False
    negator_final2 = BooleanNegator(final_val2)
    print(negator_final2.get_negated())
    print(negator_final2)
    print(negator_final2.get_original())
    print("---")
    final_val3 = True
    negator_final3 = BooleanNegator(final_val3)
    print(negator_final3.get_negated())
    print(negator_final3)
    print(negator_final3.get_original())
    print("---")
    final_val4 = False
    negator_final4 = BooleanNegator(final_val4)
    print(negator_final4.get_negated())
    print(negator_final4)
    print(negator_final4.get_original())
    print("---")
    final_val5 = True
    negator_final5 = BooleanNegator(final_val5)
    print(negator_final5.get_negated())
    print(negator_final5)
    print(negator_final5.get_original())
    print("---")
    final_val6 = False
    negator_final6 = BooleanNegator(final_val6)
    print(negator_final6.get_negated())
    print(negator_final6)
    print(negator_final6.get_original())
    print("---")
    final_val7 = True
    negator_final7 = BooleanNegator(final_val7)
    print(negator_final7.get_negated())
    print(negator_final7)
    print(negator_final7.get_original())
    print("---")
    final_val8 = False
    negator_final8 = BooleanNegator(final_val8)
    print(negator_final8.get_negated())
    print(negator_final8)
    print(negator_final8.get_original())
    print("---")
    final_val9 = True
    negator_final9 = BooleanNegator(final_val9)
    print(negator_final9.get_negated())
    print(negator_final9)
    print(negator_final9.get_original())
    print("---")
    final_val10 = False
    negator_final10 = BooleanNegator(final_val10)
    print(negator_final10.get_negated())
    print(negator_final10)
    print(negator_final10.get_original())
    print("---")
    final_val11 = True
    negator_final11 = BooleanNegator(final_val11)
    print(negator_final11.get_negated())
    print(negator_final11)
    print(negator_final11.get_original())
    print("---")
    final_val12 = False
    negator_final12 = BooleanNegator(final_val12)
    print(negator_final12.get_negated())
    print(negator_final12)
    print(negator_final12.get_original())
    print("---")
    final_val13 = True
    negator_final13 = BooleanNegator(final_val13)
    print(negator_final13.get_negated())
    print(negator_final13)
    print(negator_final13.get_original())
    print("---")
    final_val14 = False