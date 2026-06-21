from dataclasses import dataclass

@dataclass
class BooleanOperator:
    base_value: bool

    def negate(self) -> bool:
        return not self.base_value

    @staticmethod
    def validate(value: object) -> bool:
        if not isinstance(value, bool):
            raise ValueError("Value must be a boolean")
        return value

if __name__ == '__main__':
    sample_data = [True, False]
    for raw in sample_data:
        validated = BooleanOperator.validate(raw)
        operator = BooleanOperator(base_value=validated)
        print(operator.negate())