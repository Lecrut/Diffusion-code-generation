from dataclasses import dataclass
from typing import List
@dataclass
class InventoryItem:
    id: int
    name: str
    quantity: int
    def add_quantity(self, amount: int) -> None:
        if amount < 0:
            raise ValueError("Quantity cannot be decreased using this method.")
        self.quantity += amount
    def remove_quantity(self, amount: int) -> None:
        if amount < 0:
            raise ValueError("Amount cannot be negative.")
        if self.quantity - amount < 0:
            raise ValueError(f"Cannot remove {amount} units from item '{self.name}'. Only {self.quantity} available.")
        self.quantity -= amount
class InventoryManager:
    def __init__(self) -> None:
        self.items: List[InventoryItem] = []
    def add_item(self, item_id: int, name: str, quantity: int) -> InventoryItem | None:
        if quantity < 0:
            return None
        for item in self.items:
            if item.id == item_id:
                return item
        new_item = InventoryItem(id=item_id, name=name, quantity=quantity)
        self.items.append(new_item)
        return new_item
    def get_total_inventory(self) -> int:
        return sum(item.quantity for item in self.items)
if __name__ == '__main__':
    manager = InventoryManager()
    laptop_item = manager.add_item(1001, "Enterprise Laptop", 50)
    monitor_item = manager.add_item(2001, "4K Monitor", 30)
    keyboard_item = manager.add_item(3001, "Mechanical Keyboard", 75)
    laptop_item.add_quantity(20)
    monitor_item.add_quantity(10)
    print(f"Total Inventory Count: {manager.get_total_inventory()}")
    try:
        removed_keyboard = manager.items[2].remove_quantity(5)                                                                     
        print("Successfully processed sale.")
    except ValueError as e:
        print(f"Error during processing: {e}")
    final_total = manager.get_total_inventory()
    print(f"Final Inventory Count after transactions: {final_total}")