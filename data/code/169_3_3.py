class InvalidItemIDError(Exception):
    pass
class NegativeCountError(Exception):
    pass
class ItemCountManager:
    def __init__(self, valid_items):
        self.valid_items = valid_items
    def get_item_count(self, item_id, count):
        if item_id not in self.valid_items:
            raise InvalidItemIDError(f"Invalid item ID: {item_id}")
        if count < 0:
            raise NegativeCountError(f"Count cannot be negative: {count}")
        return count
if __name__ == '__main__':
    valid_items_list = [101, 102, 103]
    manager = ItemCountManager(valid_items_list)
    try:
        result1 = manager.get_item_count(101, 5)
        print(f"Count for item 101: {result1}")
    except (InvalidItemIDError, NegativeCountError) as e:
        print(f"Error: {e}")
    try:
        result2 = manager.get_item_count(999, 10)
    except (InvalidItemIDError, NegativeCountError) as e:
        print(f"Error: {e}")
    try:
        result3 = manager.get_item_count(102, -2)
    except (InvalidItemIDError, NegativeCountError) as e:
        print(f"Error: {e}")