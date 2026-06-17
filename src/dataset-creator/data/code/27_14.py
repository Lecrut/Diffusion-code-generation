import collections
class FruitClassifier:
    def __init__(self):
        self._cache = {}
        self.defaultdict_fruits = collections.defaultdict(list)
    def classify(self, fruits: list[str], grouping_key_fn=None) -> dict[str, list]:
        if not isinstance(fruits, list):
            raise TypeError("Input must be a list of strings.")
        key_signature = id(grouping_key_fn) if grouping_key_fn else None
        cache_entry = (key_signature,) + tuple(sorted([f for f in fruits]))
        if cache_entry in self._cache:
            return self._cache[cache_entry]
        result_map = collections.defaultdict(list)
        def get_group(fruit):
            if grouping_key_fn is None:
                base_groups = {
                    'citrus': ['orange', 'lemon', 'lime'],
                    'berry': ['strawberry', 'blueberry', 'blackberry'],
                    'stone': ['peach', 'plum', 'apricot']
                }
            else:
                base_groups = {
                    'citrus': ['orange', 'lemon', 'lime'],
                    'berry': ['strawberry', 'blueberry', 'blackberry'],
                    'stone': ['peach', 'plum', 'apricot']
                }
            for group_name, items in base_groups.items():
                if fruit.lower() in [item.lower() for item in items]:
                    return group_name
            unknown = f"unknown_{fruit}"
            result_map[unknown].append(fruit)
        fruits_lower = [f.lower().strip() for f in fruits]
        for i, fruit in enumerate(fruits):
            if grouping_key_fn is not None:
                try:
                    group_name = grouping_key_fn(fruit)
                except Exception as e:
                    result_map[f"error_{e}"].append((i, fruit))
                    continue
            else:
                group_name = get_group(fruit)
            if isinstance(group_name, str):
                self.defaultdict_fruits[group_name].append(fruit)
        final_result = dict(self.defaultdict_fruits)
        self._cache[cache_entry] = final_result
        return final_result
if __name__ == '__main__':
    fruits_list = ['orange', 'apple', 'banana', 'lemon', 'grape']
    classifier = FruitClassifier()
    result1 = classifier.classify(fruits_list)
    def custom_group(x):
        if x.lower().startswith('a'):
            return 'red'
        elif x.lower().startswith('l') or x.lower().startswith('o'):
            return 'yellow'
        else:
            return 'green'
    result2 = classifier.classify(fruits_list, custom_group)