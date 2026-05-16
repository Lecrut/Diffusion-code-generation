import itertools
data = [('apple', 'fruit'), ('carrot', 'vegetable'), ('banana', 'fruit'), ('broccoli', 'vegetable'), ('milk', 'dairy')]
grouped_data = {}
for key, group in itertools.groupby(data, lambda x: x[1]):
    category = key
    grouped_data[category] = list(group)
if __name__ == '__main__':
    print(grouped_data)