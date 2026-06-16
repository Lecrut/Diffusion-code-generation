from abc import ABC, abstractmethod
class ItemNameManager(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass
    @abstractmethod
    def set_name(self, name: str) -> None:
        pass
class StandardItemNameManager(ItemNameManager):
    _name = "Default"
    def __init__(self) -> None:
        self._name = "Standard Item"
    def get_name(self) -> str:
        return self._name
    def set_name(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        self._name = name
class PremiumItemNameManager(ItemNameManager):
    _prefix = "Premium"
    def __init__(self) -> None:
        super().__init__()
        self._name = f"{self._prefix} Standard Item"
    def get_name(self) -> str:
        return self._name
    def set_name(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        super().set_name(f"{self._prefix} {name}")
if __name__ == '__main__':
    standard_mgr = StandardItemNameManager()
    premium_mgr = PremiumItemNameManager()
    print(standard_mgr.get_name())                         
    standard_mgr.set_name("Custom Product")
    print(standard_mgr.get_name())                          
    print(premium_mgr.get_name())                                 
    premium_mgr.set_name("Luxury Goods")
    print(premium_mgr.get_name())