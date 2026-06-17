from dataclasses import dataclass
@dataclass(frozen=True)
class Product:
    name: str
    sku: str
    price: float
@dataclass
class InventoryItem:
    product: Product
    quantity: int = 0
    def add_quantity(self, amount: int):
        self.quantity += amount
    def remove_quantity(self, amount: int) -> bool:
        if self.quantity >= amount:
            self.quantity -= amount
            return True
        return False
if __name__ == '__main__':
    product1 = Product(name="Laptop", sku="LP-001", price=999.50)
    product2 = Product(name="Mouse", sku="MS-002", price=25.00)
    inventory = [InventoryItem(product=product1, quantity=10), InventoryItem(product=product2, quantity=5)]
    print(f"Initial Laptop count: {inventory[0].quantity}")
    inventory[0].add_quantity(5)
    print(f"After adding 5 to Laptop: {inventory[0].quantity}")
    if not inventory[1].remove_quantity(3):
        raise ValueError("Insufficient stock")
    else:
        print(f"Removed 3 from Mouse, remaining: {inventory[1].quantity}")