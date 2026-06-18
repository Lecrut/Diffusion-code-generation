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
def create_sample_inventory():
    products = [
        Product(name="Laptop", sku="LP-001", price=999.99),
        Product(name="Mouse", sku="MS-002", price=25.50),
        Product(name="Keyboard", sku="KB-003", price=75.00)
    ]
    inventory = [InventoryItem(product=p, quantity=10) for p in products]
    return inventory
if __name__ == '__main__':
    inv = create_sample_inventory()
    print(f"Initial total items: {sum(i.quantity for i in inv)}")
    inv[0].add_quantity(5)
    if not inv[1].remove_quantity(2):
        pass
    print(f"After updates - Laptop count: {inv[0].quantity}, Mouse count: {inv[1].quantity}")