class LengthMismatchError(Exception):
    def __init__(self, message, diff):
        super().__init__(message)
        self.message = message
        self.difference = diff

class RigidBodyMeasurements:
    MAX_ACCEPTABLE_RATIO = 1000.0

    def __init__(self, primary_dim, secondary_dim):
        self.primary_dim = primary_dim
        self.secondary_dim = secondary_dim

    def _validate_non_negative(self):
        if self.primary_dim < 0:
            raise ValueError("Primary dimension cannot be negative")
        if self.secondary_dim < 0:
            raise ValueError("Secondary dimension cannot be negative")

    def _check_ratio_impossibility(self, val_a, val_b):
        if val_b == 0:
            return False
        ratio = val_a / val_b
        return ratio > self.MAX_ACCEPTABLE_RATIO or ratio < (1 / self.MAX_ACCEPTABLE_RATIO)

    def evaluate_difference(self):
        self._validate_non_negative()
        diff = abs(self.primary_dim - self.secondary_dim)
        if self._check_ratio_impossibility(self.primary_dim, self.secondary_dim):
            raise LengthMismatchError(f"Dimensions differ by an impossible ratio: {diff}", diff)
        return diff

if __name__ == '__main__':
    try:
        sample_case = RigidBodyMeasurements(10.5, 5.2)
        calculated_diff = sample_case.evaluate_difference()
        print(calculated_diff)
    except LengthMismatchError as error:
        print(error.difference)
    except ValueError as error:
        print(error.args[0])
    
    try:
        edge_case = RigidBodyMeasurements(1000000.0, 1.0)
        print(edge_case.evaluate_difference())
    except LengthMismatchError as error:
        print(error.difference)
    
    try:
        invalid_case = RigidBodyMeasurements(-5, 10)
        print(invalid_case.evaluate_difference())
    except ValueError as error:
        print(error.args[0])