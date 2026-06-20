class BooleanComparator:
    TRUE = "True"
    FALSE = "False"

    @staticmethod
    def compare(a: bool, b: bool) -> str:
        if not isinstance(a, bool) or not isinstance(b, bool):
            raise ValueError("Inputs must be boolean values.")
        
        a_str = BooleanComparator.TRUE if a else BooleanComparator.FALSE
        b_str = BooleanComparator.TRUE if b else BooleanComparator.FALSE
        
        return f"{a_str} is equal to {b_str}" if a == b else f"{a_str} is not equal to {b_str}"

if __name__ == '__main__':
    result = BooleanComparator.compare(True, False)
    print(result)