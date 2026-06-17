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
            result = cd.defaultdict(list)
            for fruit in fruits:
                if fruit.lower() in classifier_map:
                    key_type, key_subtype = classifier_map[fruit.lower()]
                    result[key_type].append(fruit)
                    self.memo[id(fruits)] = (result.copy(), group_by)
        return self.memo.get(id(fruits), cd.defaultdict(list))
if __name__ == '__main__':
    clf = FruitClassifier()
    fruits_list_1 = ['apple', 'banana', 'orange']
    fruits_list_2 = ['grape', 'mango', 'apple']
    res1 = clf.classify(fruits_list_1, group_by='type')
    res2 = clf.classify(fruits_list_2, group_by='subtype')
    print(res1)
    print(res2)