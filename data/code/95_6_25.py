class AttributeValidator:
    def __init__(self, obj):
        self.obj = obj

    def is_positive(self, value):
        return value > 0

    def is_even(self, value):
        return value % 2 == 0

    def is_divisible(self, dividend, divisor):
        if divisor == 0:
            return False
        return dividend % divisor == 0

    def validate_attributes(self):
        a = self.obj.get('a', 0)
        b = self.obj.get('b', 0)
        c = self.obj.get('c', 0)
        
        positive_check = self.is_positive(a)
        even_check = self.is_even(b)
        divisible_check = self.is_divisible(c, a)
        
        return all([positive_check, even_check, divisible_check])

if __name__ == '__main__':
    sample_obj = {'a': 5, 'b': 4, 'c': 20}
    validator = AttributeValidator(sample_obj)
    print(validator.validate_attributes())