class InvalidItemIDError(Exception):
    pass
class NegativeCountError(Exception):
    pass
class ItemCountManager:
    def __init__(self, valid_items):
        self.valid_items = valid_items
    def get_item_count(self, item_id, count):
        if item_id not in self.valid_items:
            raise InvalidItemIDError(f"Item ID {item_id} is invalid.")
        if count < 0:
            raise NegativeCountError(f"Count for item {item_id} cannot be negative. Received: {count}")
        return count
if __name__ == '__main__':
    valid_ids = [101, 202, 303]
    manager = ItemCountManager(valid_ids)
    try:
        result1 = manager.get_item_count(101, 5)
        print(f"Success: Item 101 count is {result1}")
    except (InvalidItemIDError, NegativeCountError) as e:
        print(f"Error during first operation: {e}")
    try:
        result2 = manager.get_item_count(999, 10)
        print(f"Success: Item 999 count is {result2}")
    except (InvalidItemIDError, NegativeCountError) as e:
        print(f"Error during second operation: {e}")
    try:
        result3 = manager.get_item_count(202, -2)
        print(f"Success: Item 202 count is {result3}")
    except (InvalidItemIDError, NegativeCountError) as e:
        print(f"Error during third operation: {e}")