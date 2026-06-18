import collections as cd
class FruitClassifier:
    def __init__(self):
        self.memo = {}
    def classify(self, fruits, group_by='type'):
        if id(fruits) not in self.memo:
            classifier_map = {
                'apple': ('fruit', 'red'),
                'banana': ('fruit', 'yellow'),
                'orange': ('fruit', 'citrus'),
                'grape': ('fruit', 'purple'),
                'mango': ('fruit', 'tropical'),
            }
            grouped = cd.defaultdict(list)
            for fruit in fruits:
                if fruit.lower() in classifier_map:
                    key, subkey = classifier_map[fruit.lower()]
                    grouped[key].append(fruit)
            self.memo[id(fruits)] = {group_by: dict(grouped)}
        return self.memo.get(id(fruits), {}).get(group_by, {})
if __name__ == '__main__':
    fruits_list = ['apple', 'banana', 'orange', 'grape']
    classifier = FruitClassifier()
    result1 = classifier.classify(fruits_list)
    print(result1)
    modified_fruits = [fruits_list[0], fruits_list[2]]
    result2 = classifier.classify(modified_fruits, group_by='type')
    print(result2)