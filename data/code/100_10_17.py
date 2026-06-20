class LogicChecker:
    def evaluate_expression(self, expression: str) -> bool:
        try:
            result = eval(expression)
            if isinstance(result, bool):
                return result
            else:
                raise ValueError("Expression must evaluate to a boolean value")
        except SyntaxError:
            raise ValueError("Invalid syntax in the expression")
        except NameError:
            raise ValueError("Undefined name in the expression")
        except TypeError:
            raise ValueError("Unsupported type in the expression")

if __name__ == '__main__':
    checker = LogicChecker()
    print(checker.evaluate_expression("True"))
    print(checker.evaluate_expression("False"))
    print(checker.evaluate_expression("not True"))
    print(checker.evaluate_expression("5 > 3"))