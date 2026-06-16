from dataclasses import dataclass
import json
@dataclass
class Item:
    name: str
    price: float
    quantity: int
def serialize_item(item: Item) -> dict:
    return {
        "name": item.name,
        "price": item.price,
        "quantity": item.quantity
    }
def deserialize_item(data: dict) -> Item:
    return Item(
        name=data["name"],
        price=float(data["price"]),
        quantity=int(data["quantity"])
    )
if __name__ == '__main__':
    sample_items = [
        serialize_item(Item(name="Apple", price=0.5, quantity=10)),
        serialize_item(Item(name="Banana", price=0.3, quantity=20))
    ]
    json_str = json.dumps(sample_items)
    deserialized_list = []
    for item_data in sample_items:
        original_item = deserialize_item(item_data)
        deserialized_list.append(original_item)
    print(f"Original JSON:\n{json_str}")
    print("\nDeserialized Items:")
    for i, item in enumerate(deserialized_list):
        print(f"{i+1}. {item.name} - ${item.price:.2f}, Qty: {item.quantity}")