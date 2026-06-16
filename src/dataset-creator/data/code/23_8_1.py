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
        self._name_cache: dict[str, str] = {}
    def get_item_name(self) -> str:
        return self._current_name if not self._name_cache else next(iter(self._name_cache.values()))
    def set_item_name(self, name: str) -> None:
        self._current_name = name
if __name__ == '__main__':
    manager = DefaultItemNameManager()
    print(manager.get_item_name())
    manager.set_item_name("Test Item")
    print(manager.get_item_name())