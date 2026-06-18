from abc import ABC, abstractmethod
class ItemNameManager(ABC):
    @abstractmethod
    def get_item_name(self) -> str:
        pass
    @abstractmethod
    def set_item_name(self, name: str) -> None:
        pass
class DefaultItemNameManager(ItemNameManager):
    _current_name = "Default"
    def __init__(self) -> None:
        self._initialized = True
    def get_item_name(self) -> str:
        return self._current_name if hasattr(self, '_current_name') else ""
    def set_item_name(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError("Item name must be a string")
        self._current_name = name
if __name__ == '__main__':
    manager = DefaultItemNameManager()
    print(manager.get_item_name())
    manager.set_item_name("Sample Item")
    print(manager.get_item_name())