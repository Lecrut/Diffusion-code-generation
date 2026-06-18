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
    assert manager.get_name() == "Default Item"
    try:
        manager.set_name("Python Core")
        print(f"Updated Name: {manager.get_name()}")
        assert not manager.validate_name("")
        assert not manager.validate_name(123)
        assert manager.validate_name("Valid Text 456")
    except ValueError as e:
        print(f"Validation Error caught: {e}")