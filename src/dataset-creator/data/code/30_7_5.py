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
        if self.price <= 0:
            raise ValueError("price must be positive")
def validate_and_create_user(id_val, name_val, email_val) -> User:
    try:
        return User(
            id=id_val, 
            name=name_val.strip(), 
            email=email_val.strip()
        )
    except (TypeError, ValueError) as e:
        raise type(e)(f"User validation failed for {id_val}, {name_val}, {email_val}") from e
def validate_and_create_product(sku_val, price_val) -> Product:
    try:
        return Product(
            sku=sku_val.strip(), 
            price=float(price_val) if isinstance(price_val, str) else float(price_val)
        )
    except (TypeError, ValueError) as e:
        raise type(e)(f"Product validation failed for {sku_val}, {price_val}") from e
if __name__ == '__main__':
    try:
        user = validate_and_create_user(12345, "Alice Johnson", "alice@example.com")
        product = validate_and_create_product("PROD-001", 99.99)
        print(f"Created User: {user}")
        print(f"Created Product: {product}")
    except Exception as e:
        print(f"Error occurred: {e}")