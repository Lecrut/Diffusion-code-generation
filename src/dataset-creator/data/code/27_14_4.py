import collections as cd
class FruitClassifier:
    def __init__(self):
        self._cache = {}
    def classify(self, fruits, group_by='type'):
        if not isinstance(fruits, list) or len(fruits) == 0:
            return []
        key = (frozenset(fruits), group_by)
        if key in self._cache:
            return self._cache[key]
        classified = cd.defaultdict(list)
        for fruit in fruits:
            lower_fruit = str(fruit).lower()
            is_berry = any(b.lower() in lower_fruit for b in ['strawberry', 'blueberry', 'raspberry'])
            if group_by == 'type':
                category = 'Berry' if is_berry else 'Fruit'
            elif group_by == 'color':
                color_map = {'apple':'red','banana':'yellow','orange':'orange'}
                category = color_map.get(lower_fruit, 'Other')
            elif group_by == 'size':
                size_map = {'grape':'small','melon':'large','berry':'medium'}
                if any(s.lower() in lower_fruit for s in ['grape', 'melon']):
                    category = 'Large'
                else:
                    category = 'Small/Medium'
            elif group_by == 'season':
                season_map = {'apple':'winter','banana':'summer','orange':'fall'}
                if any(s.lower() in lower_fruit for s in ['apple', 'melon']):
                    category = 'Winter/Fall'
                else:
                    category = 'Summer/Spring'
            classified[category].append(fruit)
        result_list = list(classified.values())
        self._cache[key] = result_list
        return result_list
if __name__ == '__main__':
    classifier = FruitClassifier()
    sample_fruits_1 = ['apple', 'banana', 'strawberry', 'orange', 'grape']
    sample_fruits_2 = ['melon', 'blueberry', 'raspberry', 'kiwi']
    result_a = classifier.classify(sample_fruits_1, group_by='type')
    print("Group by Type:", result_a)
    result_b = classifier.classify(sample_fruits_2, group_by='color')
    print("Group by Color:", result_b)
    result_c = classifier.classify(sample_fruits_1 + sample_fruits_2, group_by='season')
    print("Combined Group by Season:", result_c)