class ValueChecker:
    def __init__(self):
        self.type_checker_map = {
            int: lambda x, y: x != y,
            float: lambda x, y: x != y,
            str: lambda x, y: x != y
        }

    def are_different(self, val1, val2):
        val1_type = type(val1)
        val2_type = type(val2)
        
        if val1_type not in self.type_checker_map or val2_type not in self.type_checker_map:
            raise ValueError(f'Unsupported type: {val1_type.__name__} or {val2_type.__name__}')
        
        return self.type_checker_map[val1_type](val1, val2)

if __name__ == '__main__':
    checker = ValueChecker()
    result_int = checker.are_different(10, 20)
    result_str = checker.are_different('hello', 'world')
    result_float = checker.are_different(3.14, 2.718)
    
    print("Integers different:", result_int)
    print("Strings different:", result_str)
    print("Floats different:", result_float)