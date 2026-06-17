import dataclasses
from typing import Any
@dataclasses.dataclass(frozen=True)
class User:
    id: int
    name: str
    email: str
    def __post_init__(self):
        if not isinstance(self.id, (int, float)):
            raise TypeError("id must be a number")
        if self.name.strip() == "":
            raise ValueError("name cannot be empty")
        if "@" not in self.email:
            raise ValueError("email is invalid")
@dataclasses.dataclass(frozen=True)
class Product:
    sku: str
    price: float
    def __post_init__(self):
        if len(self.sku.strip()) == 0:
            raise ValueError("sku cannot be empty")
        if not isinstance(self.price, (int, float)):
            raise TypeError("price must be a number")
def create_user(id_val: Any, name_val: str) -> User:
    email = f"user_{id_val}@example.com"
    return User(id=id_val, name=name_val.strip(), email=email)
if __name__ == '__main__':
    user1 = create_user(42, "Alice Smith")
    product1 = Product(sku="PROD-001", price=9.99)
    print(f"User: {user1}")
    print(f"Product: {product1}")