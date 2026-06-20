class BooleanAttribute:
    def __init__(self, value: bool):
        self.value = value

    def negate(self) -> None:
        """Negates the boolean attribute."""
        self.value = not self.value

if __name__ == '__main__':
    initial_value = True
    boolean_attr = BooleanAttribute(initial_value)
    print(f"Original Value: {boolean_attr.value}")
    boolean_attr.negate()
    print(f"Negated Value: {boolean_attr.value}")