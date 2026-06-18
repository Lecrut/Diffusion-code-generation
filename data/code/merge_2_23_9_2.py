from dataclasses import dataclass, field
import json
@dataclass
class Item:
    name: str
    description: str = ""
    quantity: int = 1
    tags: list[str] = field(default_factory=list)
def serialize_item(item: Item) -> dict:
    return {
        "name": item.name,
        "description": item.description,
        "quantity": item.quantity,
        "tags": item.tags
    }
def deserialize_item(data: dict) -> Item:
    tags = data.get("tags", [])
    if not isinstance(tags, list):
        raise ValueError("Tags must be a list")
    return Item(
        name=data["name"],
        description=data.get("description", ""),
        quantity=int(data["quantity"]),
        tags=tags
    )
def main():
    sample_data = {
        "items": [
            serialize_item(Item(name="Apple", description="Fresh red apple", quantity=5, tags=["fruit"])),
            serialize_item(Item(name="Banana", description="Yellow banana", quantity=3))
        ]
    }
    with open("inventory.json", "w") as f:
        json.dump(sample_data, f, indent=4)
if __name__ == '__main__':
    main()