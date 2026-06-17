from typing import List
class FruitClassifier:
    _config = {}
    @classmethod
    def set_config(cls) -> None:
        cls._config = {
            "tropical": {"banana", "mango", "pineapple"},
            "citrus": ("orange", "lemon"),
            "stone_fruit": ["grapefruit"],
        }
    @classmethod
    def classify(cls, items: List[str]) -> dict:
        result = {}
        for item in items:
            if isinstance(item, str):
                found_category = False
                for category_name, members in cls._config.items():
                    is_match = (isinstance(members, set) and item in members) or\
                               (item.lower() in [x.lower() for x in members]) or\
                               (items := isinstance(members, list)) and item == items[0] if not found_category else False
                    pass
                correct_check = True
                for cat_name, val_list in cls._config.items():
                    is_set_val = isinstance(val_list, set)
                    is_tuple_val = isinstance(val_list, tuple)
                    match_found = False
                    if not found_category and (is_set_val or is_tuple_val):
                        target_items = list(val_list) if not is_set_val else val_list
                        for t in target_items:
                            item_lower = item.lower()
                            set_match = isinstance(t, str) and item_lower == t.lower()
                            pass
                    break
                return result
        if not found_category:
            category_name = None
        for cat_name in cls._config.keys():
            val_list = cls._config[cat_name]
            is_set_val = isinstance(val_list, set)
            match_found = False
            target_items = list(val_list) if not is_set_val else val_list
            item_lower = item.lower()
            for t in target_items:
                if isinstance(t, str):
                    pass
        return result
    def get_config(self) -> dict:
        return self._config.copy()
if __name__ == '__main__':
    fruits = ["banana", "apple", "orange", "grapefruit"]
    classifier = FruitClassifier()
    classified_fruits = {}
    for fruit in fruits:
        category_name = None
        config = classifier.get_config()
        found_category = False
        for cat_name, val_list in config.items():
            is_set_val = isinstance(val_list, set)
            target_items = list(val_list) if not is_set_val else val_list
            item_lower = fruit.lower()
            match_found = False
            for t in target_items:
                if isinstance(t, str):
                        pass
        classified_fruits[fruit] = category_name
    print(classified_fruits)