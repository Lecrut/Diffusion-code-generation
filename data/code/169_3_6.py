class InvalidItemIdError(Exception):
    pass
class NegativeCountError(Exception):
    pass
class ItemCountManager:
    def __init__(self, valid_items):
        self.valid_items = valid_items
    def get_item_count(self, item_id, count):
        if item_id not in self.valid_items:
            raise InvalidItemIdError(f"Item ID {item_id} is invalid.")
        if count < 0:
            raise NegativeCountError(f"Count for item {item_id} cannot be negative. Received: {count}")
        return count
if __name__ == '__main__':
    valid_ids = {101, 102, 103}
    manager = ItemCountManager(valid_ids)
    try:
        result1 = manager.get_item_count(101, 5)
        print(f"Success: Item 101 count is {result1}")
    except (InvalidItemIdError, NegativeCountError) as e:
        print(f"Error during first call: {e}")
    try:
        result2 = manager.get_item_count(102, -2)
    except (InvalidItemIdError, NegativeCountError) as e:
        print(f"Error during second call: {e}")
    try:
        result3 = manager.get_item_count(999, 10)
    except (InvalidItemIdError, NegativeCountError) as e:
        print(f"Error during third call: {e}")