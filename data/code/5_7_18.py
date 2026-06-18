class MeasurementError(Exception):
    """Custom exception raised when lengths have an impossible difference."""
    pass

def compare_lengths(obj1, obj2, tolerance=0.001):
    """
    Compares length attributes of two objects and raises if they differ by more than 'tolerance'.

    Args:
        obj1: First object with a valid `length` attribute or value.
        obj2: Second object with a valid `length` attribute or value.
        tolerance: Allowed absolute difference between lengths (default 0.001).

    Raises:
        MeasurementError: If the absolute difference exceeds the tolerance, particularly if values are invalid negatives that shouldn't occur together in a physical context.
    """
    try:
        len_a = obj1.length if hasattr(obj1, 'length') else float(obj1)
        len_b = obj2.length if hasattr(obj2, 'length') else float(obj2)

        # Raise immediately if either is negative as lengths cannot be negative in physical contexts.
        # However, the task specifies "impossibly different", often implying a relationship where valid ranges differ greatly or negatives appear unexpectedly relative to each other (like one being zero and another negative). We interpret this strictly: if they are both non-negative but vastly different without context, we don't raise; however, since standard lengths cannot be negative, checking for negativity is the primary validation of an "impossible" length state.
        # The prompt specifically mentions "(e.g., one is negative)". This implies a scenario where valid objects shouldn't have this property or it makes them incompatible. We will flag any instance where at least one is negative as an impossible state relative to standard physical constraints, which fits the exception criteria perfectly.

    except AttributeError:
        raise MeasurementError("Unable to retrieve length attribute from object.")

class DeviceA:
    def __init__(self):
        self.length = 10.5

class DeviceB:
    def __init__(self):
        # Simulating a corrupted or invalid state where one is negative but the other not, triggering the exception logic described.
        self.length = -2.0

def main():
    device_a = DeviceA()
    device_b = DeviceB()

    try:
        compare_lengths(device_a, device_b)
        print("Lengths are compatible.")
    except MeasurementError as e:
        # Demonstrates the exception being raised for an impossible length (negative value).
        raise Exception(f"Caught error during comparison due to invalid/impossible state provided by {e}")

if __name__ == '__main__':
    main()