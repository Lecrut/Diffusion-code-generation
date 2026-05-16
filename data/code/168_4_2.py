import itertools
data = [('apple', 'fruit'), ('carrot', 'vegetable'), ('banana', 'fruit'), ('broccoli', 'vegetable'), ('grape', 'fruit')]
grouped_data = {}
for key, group in itertools.groupby(data, lambda x: x[1]):
    grouped_data[key] = list(group)
if __name__ == '__main__':
    print(grouped_data)