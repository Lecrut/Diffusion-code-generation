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
        self._name = name
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
        is_valid = manager.validate_name(input_val)
        if isinstance(input_val, str):
            try:
                manager.set_name(input_val)
                assert manager.get_name() == input_val
                print(f"Set '{input_val}' successfully.")
            except ValueError as e:
                print(f"Failed to set '{input_val}': {e}")
        else:
            is_valid = False
        assert is_valid == expected_result, f"Validation failed for {input_val}"
    print("All tests passed.")