from abc import ABC, abstractmethod
class ItemNameManager(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass
    @abstractmethod
    def set_name(self, name: str) -> None:
        pass
    @abstractmethod
    def validate_name(self, name: str) -> bool:
        pass
class StandardItemNameManager(ItemNameManager):
    _name = "Default Item"
    def get_name(self) -> str:
        return self._name
    def set_name(self, name: str) -> None:
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise ValueError("Name must be a non-empty string.")
        self._name = name.strip()
    def validate_name(self, name: str) -> bool:
        return isinstance(name, str) and len(name.strip()) > 0
if __name__ == '__main__':
    manager = StandardItemNameManager()
    test_cases = [
        ("Valid Name", True),
        ("   ", False),
        (123, False),
        ("Special!@#", True)
    ]
    print("Testing StandardItemNameManager:")
    assert manager.get_name() == "Default Item"
    print(f"Initial name: {manager.get_name()}")
    for input_val, expected_result in test_cases:
        try:
            is_valid = manager.validate_name(input_val)
            if not isinstance(is_valid, bool):
                raise TypeError("Validation must return a boolean.")
            if is_valid and input_val != "   ":                                                                               
                manager.set_name(input_val)
                assert manager.get_name() == input_val.strip(), f"Name mismatch after setting: {manager.get_name()} vs {input_val}"
            else:
                try:
                    manager.set_name(input_val)
                    print(f"Error: Expected exception for '{input_val}'")
                except ValueError as e:
                    assert is_valid == False, "Expected validation to fail but passed."
        except Exception as e:
            if expected_result and not isinstance(e, TypeError):
                raise AssertionError(f"Test case failed unexpectedly: {e}") from None
    print("All tests completed successfully.")