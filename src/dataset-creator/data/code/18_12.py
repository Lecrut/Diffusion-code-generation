class FruitGrouper:
    def group_fruits(self, fruit_list):
        grouped = {}
        for fruit in fruit_list:
            if fruit not in grouped:
                grouped[fruit] = []
            grouped[fruit].append(fruit)
        return grouped
if __name__ == '__main__':
    grouper = FruitGrouper()
    fruits = ["apple", "banana", "apple", "orange", "banana", "apple"]
    result = grouper.group_fruits(fruits)
    print(result)