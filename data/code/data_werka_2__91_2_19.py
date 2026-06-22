class BooleanLogic:
    DEFAULT_STATE = True

    @staticmethod
    def invert(flag: bool) -> bool:
        if not isinstance(flag, bool):
            raise ValueError("Input must be a boolean")
        return not flag

def main():
    is_active = BooleanLogic.DEFAULT_STATE
    inverted = BooleanLogic.invert(is_active)
    print(inverted)

if __name__ == '__main__':
    main()