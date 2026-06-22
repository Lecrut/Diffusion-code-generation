class ValueChecker:
    def __init__(self):
        self.type_checkers = {
            int: lambda x, y: x != y,
            float: lambda x, y: x != y,
            str: lambda x, y: x != y,
        }

    def are_different(self, val1, val2):
        type1 = type(val1)
        type2 = type(val2)

        if type1 not in self.type_checkers or type2 not in self.type_checkers:
            raise ValueError(f'Unsupported types: {type1.__name__} and {type2.__name__}')

        return self.type_checkers[type1](val1, val2) and self.type_checkers[type2](val2, val1)

if __name__ == '__main__':
    checker = ValueChecker()
    
    try:
        result_int = checker.are_different(10, 20)
        print("Integers different:", result_int)
        
        result_str = checker.are_different('hello', 'world')
        print("Strings different:", result_str)
        
        result_float = checker.are_different(3.14, 2.718)
        print("Floats different:", result_float)
        
        result_invalid = checker.are_different([1, 2], [1, 2])
    except ValueError as e:
        print(e)